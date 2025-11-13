import os
import django
from pathlib import Path

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mistico_project.settings')
django.setup()

from testes.mercado_pago_service import MercadoPagoService

print('🔍 Testando criação de preferência Mercado Pago...')

try:
    mp_service = MercadoPagoService()

    # Testar criação de preferência
    response = mp_service.criar_preferencia_pagamento(
        resposta_id=999,
        email='teste@email.com',
        teste_titulo='Teste de Pagamento',
        valor=9.90
    )

    print(f'Success: {response["success"]}')

    if response['success']:
        print('✅ Preferência criada!')
        print(f'Preference ID: {response.get("preference_id")}')
        print(f'Init Point: {response.get("init_point")}')
        print(f'Sandbox Init Point: {response.get("sandbox_init_point")}')

        if response.get('init_point'):
            print('✅ URL de checkout gerada com sucesso!')
        else:
            print('❌ URL de checkout não foi gerada')
            
        # Debug: mostrar resposta completa da API
        print('\n🔍 Debug - Chamando API diretamente...')
        try:
            preference_data = {
                "items": [
                    {
                        "title": "Teste de Pagamento",
                        "description": "Acesso ao resultado completo do seu teste espiritual",
                        "picture_url": "https://via.placeholder.com/500x500?text=Teste+Espiritual",
                        "category_id": "services",
                        "quantity": 1,
                        "currency_id": "BRL",
                        "unit_price": 9.90
                    }
                ],
                "payer": {
                    "email": "teste@email.com",
                    "name": "Cliente",
                    "surname": "Teste"
                },
                "back_urls": {
                    "success": "http://127.0.0.1:8000/pagamento/webhook/success/",
                    "failure": "http://127.0.0.1:8000/pagamento/webhook/failure/",
                    "pending": "http://127.0.0.1:8000/pagamento/webhook/pending/"
                },
                # Remover notification_url para desenvolvimento local
                # "notification_url": "http://127.0.0.1:8000/pagamento/webhook/",
                "external_reference": "resposta_999",
                # Remover auto_return para evitar erro de back_urls inválidas
                # "auto_return": "approved",
            }
            
            direct_response = mp_service.sdk.preference().create(preference_data)
            print(f'Resposta direta da API: {direct_response}')
            print(f'Status da resposta: {direct_response.get("status")}')
            print(f'Conteúdo da resposta: {direct_response.get("response")}')
            
        except Exception as api_error:
            print(f'Erro na chamada direta da API: {api_error}')
            
    else:
        print(f'❌ Erro: {response.get("error")}')

except Exception as e:
    print(f'❌ Erro de execução: {e}')
    import traceback
    traceback.print_exc()