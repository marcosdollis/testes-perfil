from django.urls import path
from . import views
from django.apps import apps

app_name = 'testes'

# Importa emails antigos quando o app é carregado
if apps.apps_ready:
    views.importar_emails_antigos()

urlpatterns = [
    path('', views.home, name='home'),
    path('emails/', views.emails_view, name='emails'),
    path('api/emails/', views.api_emails, name='api_emails'),
    path('teste/<str:tipo>/', views.teste_view, name='teste'),
    path('processar/<str:tipo>/', views.processar_teste, name='processar'),
    path('resultado/<int:resposta_id>/', views.resultado_view, name='resultado'),
    path('pagamento/<int:resposta_id>/', views.pagamento_view, name='pagamento'),
]
