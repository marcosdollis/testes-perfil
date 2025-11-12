import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db import models
from asgiref.sync import sync_to_async


class EmailConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer para listar emails em tempo real"""

    async def connect(self):
        """Conectar cliente ao canal"""
        self.room_name = 'emails'
        self.room_group_name = f'emails_{self.room_name}'

        # Adicionar ao grupo de broadcast
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Carregar TODOS os emails do banco de dados
        emails = await self.get_all_emails()
        
        # Enviar lista inicial com todos os emails
        await self.send(text_data=json.dumps({
            'type': 'initial_load',
            'emails': emails
        }))

    @sync_to_async
    def get_all_emails(self):
        """Buscar todos os emails do banco de dados"""
        try:
            from .models import Resposta
            
            # Debug: contar total de respostas
            total_respostas = Resposta.objects.count()
            print(f"[DEBUG] Total de respostas no banco: {total_respostas}")
            
            # Debug: contar emails não vazios
            emails_count = Resposta.objects.exclude(email='').count()
            print(f"[DEBUG] Total de respostas com email: {emails_count}")
            
            emails = list(
                Resposta.objects
                .filter(email__isnull=False)
                .exclude(email='')
                .values_list('email', flat=True)
                .distinct()
                .order_by('email')
            )
            
            print(f"[DEBUG] Emails únicos carregados: {len(emails)}")
            print(f"[DEBUG] Primeiros emails: {emails[:5] if emails else 'Nenhum'}")
            
            return emails
        except Exception as e:
            print(f"[ERRO] Ao buscar emails: {e}")
            import traceback
            traceback.print_exc()
            return []

    async def disconnect(self, close_code):
        """Remover cliente do grupo ao desconectar"""
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def email_message(self, event):
        """Enviar novo email para o cliente"""
        try:
            message = event.get('message', {})
            await self.send(text_data=json.dumps(message))
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
