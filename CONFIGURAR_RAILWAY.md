# 🚀 Configuração Final - Mercado Pago no Railway

## ✅ Suas Credenciais (SEGURAS - NÃO COMPARTILHE)

```
Public Key:
APP_USR-9b7dd7dd-d977-463f-8873-ac2559a75809

Access Token:
APP_USR-7960719101787621-111220-80af955db1e49dcaa56accbc2b57c122-192104726
```

## 📋 Passo a Passo: Adicionar no Railway

### 1️⃣ Acesse o Railway Dashboard
- URL: https://railway.app/dashboard
- Clique no seu projeto **testes-perfil**

### 2️⃣ Vá em **Settings**
- Clique na engrenagem ⚙️ (Settings) na barra superior
- Ou clique em **Settings** no menu lateral

### 3️⃣ Clique em **Variables**
- No menu lateral, procure por "Variables"
- Você verá a lista de variáveis já configuradas

### 4️⃣ Adicione as 3 variáveis do Mercado Pago

**Clique em "+ Add Variable" 3 vezes e preencha:**

#### Variável 1:
```
Chave: MERCADO_PAGO_ACCESS_TOKEN
Valor: APP_USR-7960719101787621-111220-80af955db1e49dcaa56accbc2b57c122-192104726
```

#### Variável 2:
```
Chave: MERCADO_PAGO_PUBLIC_KEY
Valor: APP_USR-9b7dd7dd-d977-463f-8873-ac2559a75809
```

#### Variável 3:
```
Chave: MERCADO_PAGO_NOTIFICATION_URL
Valor: https://seu-app.up.railway.app/pagamento/webhook/notification/
```

⚠️ **IMPORTANTE:** Substitua `seu-app` pelo nome real do seu app no Railway!

### 5️⃣ Salvar
- Clique em **Save** ou **Deploy**
- Railway vai fazer redeploy automaticamente

## ✅ Verificar se Funcionou

### Teste Local (Opcional)
```bash
python test_mercado_pago.py
```

### Teste no Railway
1. Acesse seu app: `https://seu-app.up.railway.app`
2. Faça um teste qualquer
3. Vá para resultado e clique em "Finalizar"
4. Você deve ver o botão: **💳 Pagar com Mercado Pago**
5. Clique nele - deve redirecionar para checkout do Mercado Pago

## 🎉 Pronto!

Agora seu sistema está:
- ✅ Fazendo testes
- ✅ Salvando emails em tempo real
- ✅ Mostrando resultados personalizados
- ✅ **ACEITANDO PAGAMENTOS** via Mercado Pago

## 💳 Próximo Passo: Testar um Pagamento

1. Acesse seu site
2. Complete um teste
3. Clique em "Finalizar"
4. Use um cartão de teste:
   - **Visa:** 4111 1111 1111 1111
   - **Mastercard:** 5555 5555 5555 4444
   - **Data:** Qualquer data futura (ex: 12/25)
   - **CVV:** 123

## 🔐 Segurança

- ✅ Credenciais seguras no Railway (não no GitHub)
- ✅ Pagamentos criptografados
- ✅ Webhook seguro
- ✅ Dados do usuário protegidos

## 📞 Se der erro:

1. Verifique se as variáveis foram salvas
2. Aguarde 2-3 minutos para Railway fazer redeploy
3. Verifique os logs: Railway → Logs
4. Procure por mensagens de erro sobre Mercado Pago
