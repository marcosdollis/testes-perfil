from django.apps import AppConfig


class TestesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testes'
    
    def ready(self):
        # Importa sinais que mantêm sincronização adicional (apêndice em arquivo opcional)
        try:
            from . import signals  # noqa: F401
        except Exception:
            pass
