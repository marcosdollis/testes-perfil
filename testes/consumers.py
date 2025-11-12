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
            emails = list(
                Resposta.objects
                .filter(email__isnull=False)
                .exclude(email='')
                .values_list('email', flat=True)
                .distinct()
                .order_by('email')
            )
            return emails
        except Exception as e:
            print(f"Erro ao buscar emails: {e}")
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
