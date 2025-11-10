from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os

from .models import Resposta


@receiver(post_save, sender=Resposta)
def resposta_saved(sender, instance, created, **kwargs):
    """Ação executada quando uma Resposta é criada.

    - Mantemos um apêndice opcional em `emails_registrados.txt` quando em DEBUG local
      ou quando a variável `WRITE_EMAIL_FILE=True` estiver ativa.
    - Não realiza chamadas externas para não expor credenciais.
    """
    if not created:
        return

    email = getattr(instance, 'email', '')
    if not email:
        return

    write_file = os.environ.get('WRITE_EMAIL_FILE', 'False') == 'True'
    if getattr(settings, 'DEBUG', False) or write_file:
        try:
            with open('emails_registrados.txt', 'a', encoding='utf-8') as f:
                f.write(f"{email}\n")
        except Exception:
            # Não bloquear o fluxo principal por problema de I/O
            pass
