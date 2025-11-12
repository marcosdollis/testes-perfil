from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import os
import json

from .models import Resposta


@receiver(post_save, sender=Resposta)
def resposta_saved(sender, instance, created, **kwargs):
    """Ação executada quando uma Resposta é criada.

    - Mantemos um apêndice opcional em `emails_registrados.txt` quando em DEBUG local
      ou quando a variável `WRITE_EMAIL_FILE=True` estiver ativa.
    - Faz broadcast do novo email para todos os clientes WebSocket conectados
    - Não realiza chamadas externas para não expor credenciais.
    """
    if not created:
        return

    email = getattr(instance, 'email', '')
    if not email:
        return

    # Salvar em arquivo local se em DEBUG
    write_file = os.environ.get('WRITE_EMAIL_FILE', 'False') == 'True'
    if getattr(settings, 'DEBUG', False) or write_file:
        try:
            with open('emails_registrados.txt', 'a', encoding='utf-8') as f:
                f.write(f"{email}\n")
        except Exception:
            # Não bloquear o fluxo principal por problema de I/O
            pass

    # Fazer broadcast para todos os clientes WebSocket
    try:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'emails_emails',
            {
                'type': 'email_message',
                'message': {
                    'type': 'new_email',
                    'email': email
                }
            }
        )
    except Exception:
        # Não bloquear o fluxo principal se o broadcast falhar
        pass
