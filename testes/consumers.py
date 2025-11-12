import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Resposta


class EmailConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer para listar emails em tempo real"""

    async def connect(self):
        """Conectar cliente ao canal e enviar lista inicial de emails"""
        self.room_name = 'emails'
        self.room_group_name = f'emails_{self.room_name}'

        # Adicionar ao grupo de broadcast
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Enviar lista inicial de emails
        emails = await self.get_all_emails()
        await self.send(text_data=json.dumps({
            'type': 'initial_load',
            'emails': emails
        }))

    async def disconnect(self, close_code):
        """Remover cliente do grupo ao desconectar"""
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def email_message(self, event):
        """Enviar novo email para o cliente"""
        message = event['message']
        await self.send(text_data=json.dumps(message))

    @sync_to_async
    def get_all_emails(self):
        """Obter todos os emails únicos do banco"""
        emails = list(Resposta.objects.exclude(
            email=''
        ).values_list('email', flat=True).distinct().order_by('-criado_em')[:100])
        return emails
