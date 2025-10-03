from django.urls import path
from . import views

app_name = 'testes'

urlpatterns = [
    path('', views.home, name='home'),
    path('teste/<str:tipo>/', views.teste_view, name='teste'),
    path('processar/<str:tipo>/', views.processar_teste, name='processar'),
    path('resultado/<int:resposta_id>/', views.resultado_view, name='resultado'),
    path('pagamento/<int:resposta_id>/', views.pagamento_view, name='pagamento'),
]
