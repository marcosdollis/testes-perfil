# 🚀 Deploy no Railway.app - Guia Completo

## ✅ Preparação Concluída!

Seu projeto Django está pronto para deploy no Railway com SQLite.

---

## 📋 Passo a Passo para Deploy

### 1️⃣ **Criar Conta no Railway**
- Acesse: https://railway.app/
- Clique em "Start a New Project"
- Faça login com GitHub

### 2️⃣ **Subir Código para GitHub**

```bash
# No terminal do seu projeto:
cd "c:\Users\Marcos\Documents\python projects\testes-perfil"

# Inicializar Git (se ainda não foi)
git init

# Adicionar arquivos
git add .

# Commit
git commit -m "Projeto pronto para deploy no Railway"

# Criar repositório no GitHub e conectar
# (Vá em github.com/new e crie um repo)
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git branch -M main
git push -u origin main
```

### 3️⃣ **Deploy no Railway**

1. No Railway, clique em **"New Project"**
2. Selecione **"Deploy from GitHub repo"**
3. Escolha seu repositório
4. Railway vai detectar Django automaticamente!

### 4️⃣ **Configurar Variáveis de Ambiente**

No Railway, vá em **Settings → Variables** e adicione:

```
SECRET_KEY=seu-secret-key-aleatorio-super-seguro-aqui-12345
DEBUG=False
ALLOWED_HOSTS=*.railway.app,seudominio.com
PYTHONUNBUFFERED=1
```

**⚠️ IMPORTANTE:** Gere um SECRET_KEY seguro:
```python
# Execute isso para gerar:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5️⃣ **Configurar Volume Persistente (ESSENCIAL para SQLite)**

No Railway:
1. Vá na aba **"Data"** ou **"Volumes"**
2. Clique em **"Add Volume"**
3. Configure:
   - **Mount Path**: `/app/data`
   - Isso garante que o SQLite não seja apagado nos redeploys

4. **Atualizar settings.py** (ou criar settings_prod.py):
```python
# Adicionar essa linha no DATABASES:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/data/db.sqlite3',  # Salva no volume persistente
    }
}
```

### 6️⃣ **Deploy Automático**

- Railway vai fazer build e deploy automaticamente
- Aguarde ~2-3 minutos
- Acesse a URL que o Railway fornecer (ex: `seu-app.railway.app`)

---

## 🔧 Comandos Úteis

### Coletar arquivos estáticos (Railway faz automaticamente):
```bash
python manage.py collectstatic --no-input
```

### Rodar migrações (Railway faz automaticamente):
```bash
python manage.py migrate
```

### Ver logs no Railway:
- Vá na aba "Deployments" → Clique no deploy → "View Logs"

---

## 💰 Custos Estimados (Plano Free)

- **$5 grátis/mês**
- **~$0.50/mês** para app pequeno (sempre online)
- **Sobra ~$4.50** para tráfego

### Quando você vai ultrapassar o free tier:
- **~500-1000 visitas/dia** = Ainda dentro do free
- **>5.000 visitas/dia** = Pode precisar pagar ($5-10/mês)

---

## 🎯 Checklist Final

Antes de fazer deploy, certifique-se:

- [ ] SECRET_KEY configurado no Railway
- [ ] DEBUG=False em produção
- [ ] ALLOWED_HOSTS configurado
- [ ] Volume persistente criado para SQLite
- [ ] requirements.txt atualizado
- [ ] Procfile criado
- [ ] .gitignore configurado (não subir db.sqlite3 do local)

---

## ⚠️ IMPORTANTE: SQLite no Railway

**Vantagens:**
✅ Simples, sem custo adicional
✅ Funciona perfeitamente para tráfego baixo-médio
✅ Não precisa configurar PostgreSQL

**Limitações:**
⚠️ Um servidor (não escala horizontalmente)
⚠️ Para tráfego MUITO alto (>10k usuários simultâneos), considere PostgreSQL
⚠️ Backups manuais (baixe o db.sqlite3 periodicamente)

**Para backup do banco:**
```bash
# No Railway CLI:
railway run python manage.py dumpdata > backup.json

# Ou baixe o arquivo db.sqlite3 via SFTP/SSH
```

---

## 🚨 Troubleshooting

### Erro: "Application failed to respond"
- Verifique se PORT está configurado corretamente no Procfile
- Confira os logs: Railway → Deployments → View Logs

### Erro: "DisallowedHost"
- Adicione o domínio do Railway no ALLOWED_HOSTS

### Erro: "Static files not found"
- Execute: `python manage.py collectstatic`
- Verifique WhiteNoise no MIDDLEWARE

### Banco de dados resetando:
- **CRIE O VOLUME PERSISTENTE!** (Passo 5)
- Sem volume, o SQLite é apagado a cada deploy

---

## 📞 Suporte

- Railway Docs: https://docs.railway.app/
- Railway Discord: https://discord.gg/railway
- Railway Status: https://status.railway.app/

---

## 🎉 Pronto!

Seu site estará online em: `https://seu-app.railway.app`

Boa sorte com o lançamento! 🚀💰
