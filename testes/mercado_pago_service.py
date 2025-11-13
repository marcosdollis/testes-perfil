"""
Serviço de integração com Mercado Pago
"""
import mercadopago
from django.conf import settings
from django.urls import reverse
import json
import logging

logger = logging.getLogger(__name__)


class MercadoPagoService:
    def __init__(self):
        """Inicializar cliente do Mercado Pago"""
        self.sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
    
    def criar_preferencia_pagamento(self, resposta_id, email, teste_titulo, valor=9.90):
        """
        Criar preferência de pagamento no Mercado Pago
        
        Args:
            resposta_id: ID da resposta do teste
            email: Email do usuário
            teste_titulo: Título do teste
            valor: Valor a pagar em reais
            
        Returns:
            dict com init_point (URL de checkout) ou erro
        """
        try:
            # Dados da preferência
            preference_data = {
                "items": [
                    {
                        "title": f"Resultado Completo - {teste_titulo}",
                        "description": "Acesso ao resultado completo do seu teste espiritual",
                        "picture_url": "https://via.placeholder.com/500x500?text=Teste+Espiritual",
                        "category_id": "services",
                        "quantity": 1,
                        "currency_id": "BRL",
                        "unit_price": float(valor)
                    }
                ],
                "payer": {
                    "email": email,
                    "name": "Cliente",
                    "surname": "Teste"
                },
                "back_urls": {
                    "success": f"{settings.MERCADO_PAGO_NOTIFICATION_URL}success/",
                    "failure": f"{settings.MERCADO_PAGO_NOTIFICATION_URL}failure/",
                    "pending": f"{settings.MERCADO_PAGO_NOTIFICATION_URL}pending/"
                },
                "notification_url": settings.MERCADO_PAGO_NOTIFICATION_URL,
                "external_reference": f"resposta_{resposta_id}",
                "auto_return": "approved",
            }
            
            # Criar preferência
            response = self.sdk.preference().create(preference_data)
            
            logger.info(f"Preferência Mercado Pago criada: {response['response'].get('id')}")
            
            return {
                'success': True,
                'preference_id': response['response'].get('id'),
                'init_point': response['response'].get('init_point'),
                'sandbox_init_point': response['response'].get('sandbox_init_point'),
            }
        except Exception as e:
            logger.error(f"Erro ao criar preferência Mercado Pago: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def obter_pagamento(self, payment_id):
        """
        Obter informações de um pagamento
        
        Args:
            payment_id: ID do pagamento
            
        Returns:
            dict com informações do pagamento ou erro
        """
        try:
            response = self.sdk.payment().get(payment_id)
            return {
                'success': True,
                'payment_data': response['response']
            }
        except Exception as e:
            logger.error(f"Erro ao obter pagamento {payment_id}: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def processar_webhook(self, payment_id):
        """
        Processar notificação de webhook do Mercado Pago
        
        Args:
            payment_id: ID do pagamento
            
        Returns:
            dict com status do processamento
        """
        try:
            from .models import Resposta
            from django.utils import timezone
            
            # Obter dados do pagamento
            payment_info = self.obter_pagamento(payment_id)
            
            if not payment_info['success']:
                return {'success': False, 'error': 'Pagamento não encontrado'}
            
            payment_data = payment_info['payment_data']
            external_reference = payment_data.get('external_reference', '')
            status = payment_data.get('status', 'pending')
            
            # Extrair ID da resposta
            if not external_reference.startswith('resposta_'):
                return {'success': False, 'error': 'Referência inválida'}
            
            resposta_id = int(external_reference.split('_')[1])
            
            # Atualizar resposta
            resposta = Resposta.objects.get(id=resposta_id)
            resposta.payment_id = payment_id
            resposta.payment_status = status
            resposta.payment_method = payment_data.get('payment_method', {}).get('type', 'unknown')
            resposta.payment_amount = float(payment_data.get('transaction_amount', 0))
            
            if status == 'approved':
                resposta.pago = True
                resposta.pago_em = timezone.now()
            
            resposta.save()
            
            logger.info(f"Pagamento {payment_id} processado com status: {status}")
            
            return {
                'success': True,
                'resposta_id': resposta_id,
                'payment_status': status
            }
        except Exception as e:
            logger.error(f"Erro ao processar webhook: {e}")
            return {
                'success': False,
                'error': str(e)
            }
