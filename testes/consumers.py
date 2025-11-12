import json
from channels.generic.websocket import AsyncWebsocketConsumer


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

        # Enviar inicial vazio - os emails virão via broadcast
        await self.send(text_data=json.dumps({
            'type': 'initial_load',
            'emails': []
        }))

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
