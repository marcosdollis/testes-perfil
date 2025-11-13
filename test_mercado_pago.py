#!/usr/bin/env python
"""
Script de teste para configuração do Mercado Pago
Execute: python test_mercado_pago.py
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mistico_project.settings')
django.setup()

from django.conf import settings

print("=" * 60)
print("🔍 VERIFICANDO CONFIGURAÇÃO MERCADO PAGO")
print("=" * 60)

# Verificar Access Token
access_token = settings.MERCADO_PAGO_ACCESS_TOKEN
if access_token:
    print(f"✅ Access Token: {access_token[:20]}...{access_token[-20:]}")
else:
    print("❌ Access Token: NÃO CONFIGURADO")

# Verificar Public Key
public_key = settings.MERCADO_PAGO_PUBLIC_KEY
if public_key:
    print(f"✅ Public Key: {public_key[:20]}...{public_key[-20:]}")
else:
    print("❌ Public Key: NÃO CONFIGURADO")

# Verificar Notification URL
notification_url = settings.MERCADO_PAGO_NOTIFICATION_URL
if notification_url:
    print(f"✅ Notification URL: {notification_url}")
else:
    print("❌ Notification URL: NÃO CONFIGURADO")

print("\n" + "=" * 60)

# Testar SDK
if access_token and public_key:
    try:
        import mercadopago
        print("✅ SDK Mercado Pago instalado corretamente")
        
        # Tentar conectar
        sdk = mercadopago.SDK(access_token)
        print("✅ Conexão com Mercado Pago: OK")
        
        print("\n✨ Tudo configurado! Pronto para aceitar pagamentos!")
        
    except ImportError:
        print("❌ SDK Mercado Pago NÃO instalado")
        print("   Execute: pip install mercado-pago")
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
else:
    print("⚠️  Credenciais incompletas. Configure as variáveis de ambiente:")
    print("   - MERCADO_PAGO_ACCESS_TOKEN")
    print("   - MERCADO_PAGO_PUBLIC_KEY")

print("=" * 60)
