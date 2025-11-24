# 🔧 Guia de Troubleshooting - Deploy no Railway

## ❌ Problema: Deploy não está funcionando

Se você está vendo erro no Railway ou o site não carrega, siga estes passos:

---

## 1️⃣ VERIFICAR LOGS DO RAILWAY

### No Dashboard do Railway:
1. Acesse https://railway.app
2. Clique no seu projeto
3. Clique na aba **"Logs"** (no painel de direita)
4. Procure por mensagens de erro (linha vermelha)

**Erros comuns:**
- `ModuleNotFoundError` → Faltam dependências
- `ImproperlyConfigured` → Faltam variáveis de ambiente
- `ConnectionRefusedError` → Banco de dados não conecta

---

## 2️⃣ VARIÁVEIS DE AMBIENTE OBRIGATÓRIAS

No Railway, clique em **"Variables"** e adicione:

```
DEBUG=False
SECRET_KEY=seu-secret-key-gerado
ALLOWED_HOSTS=*.railway.app
PYTHONUNBUFFERED=1
DATABASE_PATH=/app/data/db.sqlite3
```

---

## 3️⃣ PROBLEMA: "ModuleNotFoundError"

**Causa:** Faltam dependências instaladas

**Solução:**
1. Verifique se `requirements.txt` tem todas as dependências:
   ```
   Django>=5.2.0
   Pillow>=10.0.0
   gunicorn>=21.2.0
   whitenoise>=6.6.0
   dj-database-url>=1.0.0
   psycopg2-binary>=2.9.6
   channels>=4.3.0
   channels-redis>=4.3.0
   daphne>=4.2.0
   mercadopago>=2.0.0
   python-dotenv>=1.0.0
   ```

2. Se adicionou algo novo, faça push novamente:
   ```bash
   git add requirements.txt
   git commit -m "Adicionar dependências"
   git push origin master
   ```

---

## 4️⃣ PROBLEMA: "Collectstatic" falhando

Se vê erro sobre `collectstatic` nos logs:

**Solução:** Configure o Railway para pular collectstatic:
1. Nas **Variables**, adicione:
   ```
   SKIP_COLLECTSTATIC=1
   ```

---

## 5️⃣ PROBLEMA: Banco de dados não conecta

**Se está usando SQLite persistente:**
1. Nas **Variables**, adicione:
   ```
   DATABASE_PATH=/app/data/db.sqlite3
   ```

2. Na aba **"Settings"**, clique em **"Volumes"**
3. Adicione um volume: `/app/data`

---

## 6️⃣ FORÇAR REDEPLOY MANUAL

Se nada funcionar, force um redeploy:

1. Acesse o **Railway Dashboard**
2. Clique no seu projeto
3. Clique em **"Deployments"**
4. Clique no último deploy (com ✓)
5. Clique em **"Redeploy"**

---

## 7️⃣ VERIFICAR URL DO SITE

Após o deploy:
1. No Railway Dashboard
2. Clique em **"Domains"**
3. Procure pela URL `*.railway.app`
4. Acesse no navegador

---

## 8️⃣ TESTE LOCAL ANTES DE FAZER PUSH

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Testar localmente
python manage.py runserver
```

Se funcionar local, deve funcionar no Railway!

---

## 9️⃣ CHECKLIST FINAL

- [ ] Todas as variáveis de ambiente estão no Railway
- [ ] `requirements.txt` tem todas as dependências
- [ ] `Procfile` está correto
- [ ] `railway.json` está correto
- [ ] URLs estão em `ALLOWED_HOSTS`
- [ ] Banco de dados está configurado (volume)
- [ ] Último push foi bem-sucedido (check no GitHub)

---

## 🆘 AINDA NÃO FUNCIONA?

1. Verifique os **Logs** do Railway (aba Logs)
2. Copie a mensagem de erro exata
3. Procure no Google: `railway django [sua-mensagem-de-erro]`
4. Ou abra uma issue no repositório com o erro completo

---

**Última atualização:** 24/11/2025
