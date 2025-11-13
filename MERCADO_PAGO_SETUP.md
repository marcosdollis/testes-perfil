# 💳 Configuração do Mercado Pago

## Informações Fornecidas

✅ **Public Key (Chave Pública):**
```
APP_USR-9b7dd7dd-d977-463f-8873-ac2559a75809
```

## ❓ O que falta:

Você precisa do **Access Token** (Token de Acesso).

### Como obter no Mercado Pago:

1. **Acesse:** https://www.mercadopago.com.br/developers/panel/credentials
2. **Faça login** com sua conta
3. **Na aba "Credenciais"** procure por:
   - **Token de Acesso** (Production) ou **Access Token**
   - Deve começar com `APP_USR-` seguido de um UUID

Ele terá este formato:
```
APP_USR-xxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
```

## 📝 Configurar no Railway

Após obter o Access Token, faça assim:

### 1️⃣ Acesse o Railroad Dashboard
- https://railway.app/dashboard
- Clique no seu projeto

### 2️⃣ Vá em Settings → Variables

### 3️⃣ Adicione as seguintes variáveis:

| Variável | Valor |
|----------|-------|
| `MERCADO_PAGO_ACCESS_TOKEN` | `APP_USR-xxxxxx...` (seu token) |
| `MERCADO_PAGO_PUBLIC_KEY` | `APP_USR-9b7dd7dd-d977-463f-8873-ac2559a75809` |
| `MERCADO_PAGO_NOTIFICATION_URL` | `https://seu-app.up.railway.app/pagamento/webhook/notification/` |

### 4️⃣ Salve e o Railway vai fazer redeploy automaticamente

## 🧪 Testando

Após configurar:

1. Acesse seu app: `https://seu-app.up.railway.app`
2. Faça um teste
3. Vá para resultado e clique em "Finalizar"
4. Verifique se o botão "💳 Pagar com Mercado Pago" aparece

## 🔐 Segurança

- ✅ Nunca compartilhe seu **Access Token**
- ✅ Nunca comite credenciais no GitHub
- ✅ Use apenas variáveis de ambiente no Railway
- ✅ A Public Key pode ser pública (é usada no frontend)

## 📞 Precisa de Ajuda?

Se o checkout não funcionar, verifique:
1. As credenciais estão corretas?
2. Variáveis foram salvas no Railway?
3. Railway fez o redeploy?
4. Verifique os logs: Railway Dashboard → Logs
