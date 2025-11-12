# 🚀 Guia Completo: Deploy no Railway

Este projeto está **100% pronto** para deploy no Railway com suporte completo a **WebSocket em tempo real**.

## ✅ Pré-requisitos

- Conta no GitHub (você já tem) ✅
- Conta no Railway (gratuita em https://railway.app) 
- Projeto já no GitHub (marcosdollis/testes-perfil) ✅

---

## 📋 Passo 1: Conectar o Repositório ao Railway

1. Acesse https://railway.app/dashboard
2. Clique em **"New Project"** (ou **"Create"**)
3. Selecione **"Deploy from GitHub repo"**
4. Autorize o Railway a acessar sua conta GitHub
5. Escolha o repositório **marcosdollis/testes-perfil**
6. Clique em **"Deploy"**

Railway vai detectar automaticamente que é um projeto Django e começar o build.

---

## 🗄️ Passo 2: Adicionar Banco de Dados PostgreSQL

1. No painel do Railway (após deploy iniciado)
2. Clique em **"Add Service"** ou **"+ New"**
3. Escolha **"Database"** → **"PostgreSQL"**
4. Railway vai criar automaticamente e adicionar a variável `DATABASE_URL`

**Verificar a conexão:**
- Vá em **Variables** do seu app
- Procure por `DATABASE_URL` (deve estar lá automaticamente)

---

## ⚙️ Passo 3: Configurar Variáveis de Ambiente

No Railway, vá em seu app → **Settings** → **Variables** e adicione/configure:

### Variáveis obrigatórias:

```
SECRET_KEY = <gere um valor seguro>
DEBUG = False
ALLOWED_HOSTS = seu-app-name.up.railway.app,seu-dominio-customizado.com
DATABASE_URL = <será criada automaticamente pelo plugin Postgres>
```

### Para gerar um SECRET_KEY seguro localmente:

```powershell
.\venv\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copie o valor gerado e cole em `SECRET_KEY` no Railway.

### Variáveis opcionais:

```
WRITE_EMAIL_FILE = False  (não gravar arquivo local em produção)
PYTHONUNBUFFERED = 1      (mostrar logs em tempo real)
```

---

## 🔌 Passo 4: Verificar Deploy

1. Acesse o link do seu app (ex: `seu-app-name.up.railway.app`)
2. Você deve ver a **página inicial** dos testes de personalidade ✅
3. Acesse `/emails/` para ver o dashboard em tempo real
4. Submeta um teste com seu email
5. Veja o email aparecer **instantaneamente** em tempo real no dashboard! 🎉

---

## 📊 Arquitetura do Deploy

```
┌─────────────────────────────────────┐
│     Railway (seu-app.railway.app)   │
├─────────────────────────────────────┤
│  ✅ Django 5.2.8                    │
│  ✅ Daphne (ASGI + WebSocket)       │
│  ✅ PostgreSQL                      │
│  ✅ Static Files (WhiteNoise)       │
└─────────────────────────────────────┘
        ↓ (via git push)
┌─────────────────────────────────────┐
│   GitHub (marcosdollis/testes-...) │
│   (seu repositório)                 │
└─────────────────────────────────────┘
```

### Fluxo de dados em tempo real:

1. **Usuário submete teste** → Django grava em PostgreSQL
2. **Django signal ativa** → Broadcast via WebSocket para todos os clientes
3. **Dashboard atualiza** → Novo email aparece em TEMPO REAL ⚡

---

## 🧪 Testando Localmente Antes do Deploy

```powershell
# Inicie o servidor local (com WebSocket)
.\venv\Scripts\python.exe manage.py runserver

# Abra em dois navegadores:
# - Um para submeter testes: http://localhost:8000/
# - Outro para ver dashboard: http://localhost:8000/emails/

# Submeta um teste e veja o email aparecer em tempo real no dashboard!
```

---

## ❌ Troubleshooting no Railway

### "Application failed to respond"
- Verifique os logs: Railway → Deployments → View Logs
- Procure por erros de importação ou configuração

### "DisallowedHost at /emails/"
- Adicione seu domínio em `ALLOWED_HOSTS` nas Variables

### "WebSocket connection refused"
- Certifique-se que o `Procfile` está usando Daphne (não gunicorn)
- Verifique se `channels` e `daphne` estão em `requirements.txt`

### Emails não aparecem em tempo real
- Certifique-se que `DATABASE_URL` está configurada
- Verifique se o PostgreSQL plugin foi adicionado
- Veja os logs do servidor para mensagens de erro

---

## 📈 Monitorando em Tempo Real

1. No Railway, clique em **"View Logs"** para ver logs do servidor
2. Você verá:
   - Requisições HTTP
   - Conexões WebSocket
   - Queries do banco de dados

---

## 🔐 Segurança em Produção

✅ `DEBUG = False` (desabilita debug mode)  
✅ `ALLOWED_HOSTS` configurado (previne Host Header Attacks)  
✅ `SECRET_KEY` seguro (gerado aleatoriamente)  
✅ HTTPS automático (Railway fornece certificado SSL)  
✅ PostgreSQL em banco remoto (não SQLite local)  
✅ Static files servidos via WhiteNoise  

---

## 📱 Acessando de Outros Dispositivos

Após fazer deploy no Railway:

```
Computador A: https://seu-app-name.up.railway.app/
Computador B: https://seu-app-name.up.railway.app/emails/

Submeta um teste em A e veja em tempo real em B!
```

---

## 💾 Backups do Banco de Dados

Railway automaticamente faz backups diários do PostgreSQL. Para exportar dados manualmente:

```powershell
# Via Railway CLI:
railway run python manage.py dumpdata > backup.json

# Ou acesse o PostgreSQL diretamente com ferramentas como pgAdmin
```

---

## 🚀 Próximos Passos (Opcional)

- [ ] Configurar domínio customizado no Railway
- [ ] Adicionar autenticação de usuários
- [ ] Implementar pagamentos (Stripe, PayPal, etc)
- [ ] Exportar emails para Google Drive/S3
- [ ] Adicionar mais testes de personalidade

---

## 📞 Suporte

- **Railway Docs**: https://docs.railway.app/
- **Django Channels**: https://channels.readthedocs.io/
- **Este Projeto**: https://github.com/marcosdollis/testes-perfil

---

## ✨ Resumo: O Que Você Tem

✅ **Testes de Personalidade** (Personalidade, QI, Renda, Signos)  
✅ **Dashboard em Tempo Real** (WebSocket)  
✅ **Banco de Dados Remoto** (PostgreSQL)  
✅ **Migração Automática** (ao fazer deploy)  
✅ **HTTPS/SSL** (gratuito no Railway)  
✅ **Pronto para Produção** (configurado corretamente)  

Seu projeto está **100% pronto para ir ao ar!** 🎉

---

**Última atualização**: 12 de Novembro de 2025
