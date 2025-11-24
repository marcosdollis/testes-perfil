# 🚂 GUIA PASSO A PASSO: Deploy no Railway

## ❌ Seu site não está aparecendo depois do push?

Siga estes passos para resolver:

---

## PASSO 1: Abrir o Railway Dashboard

1. Acesse https://railway.app
2. Faça login com sua conta
3. Clique no seu projeto **"testes-perfil"**

---

## PASSO 2: Verificar o Status do Deploy

No painel principal, procure pela seção **"Deployments"**:

- ✅ **Verde/Success** = Deploy foi bem-sucedido
- ⏳ **Amarelo/In Progress** = Deploy ainda está rodando (aguarde 2-3 minutos)
- ❌ **Vermelho/Failed** = Deploy falhou (veja os logs abaixo)

---

## PASSO 3: Ver os Logs (MUITO IMPORTANTE!)

1. Clique na aba **"Logs"** (canto superior direito)
2. Procure por mensagens vermelhas ou de erro
3. **Copie a mensagem de erro** (inteira!)

### Erros mais comuns:

**A) `ImproperlyConfigured: DEBUG may not be enabled when deploying`**
- **Causa**: DEBUG=True em produção
- **Solução**: Vá em "Variables" e mude para `DEBUG=False`

**B) `ModuleNotFoundError: No module named 'testes'`**
- **Causa**: Arquivo de configuração errado
- **Solução**: Verifique se `railway.json` está correto

**C) `Connection refused` ao banco de dados**
- **Causa**: Banco de dados não está configurado
- **Solução**: Vá em "Variables" e adicione as variáveis de banco

**D) `SyntaxError` ou `ImportError`**
- **Causa**: Erro no código Python
- **Solução**: Verifique o arquivo de erro mencionado nos logs

---

## PASSO 4: Configurar Variáveis de Ambiente (CRÍTICO!)

1. No Dashboard do Railway, procure por **"Variables"** (ou engrenagem ⚙️)
2. Clique em **"New Variable"**
3. **Adicione EXATAMENTE estas variáveis:**

```
DEBUG=False
SECRET_KEY=u1&f1u_@c@mzkw4-2&+u#%9v%_f0e%6!$f3ov+yp0py0626y_4
ALLOWED_HOSTS=*.railway.app
PYTHONUNBUFFERED=1
```

⚠️ **IMPORTANTE:** Após adicionar as variáveis, o Railway vai fazer redeploy automático!

---

## PASSO 5: Aguardar o Deploy

Após adicionar as variáveis:

1. Volte para **"Logs"**
2. Aguarde a mensagem: `Application is running on ...`
3. Isso significa que está online!
4. **Aguarde 2-3 minutos** antes de testar

---

## PASSO 6: Encontrar a URL do Seu Site

1. Na aba **"Domains"** (ou "Settings")
2. Procure pela URL que parece com: `https://seu-app-xxxx.up.railway.app`
3. **Copie esta URL**
4. Abra em uma **nova aba** do navegador

---

## PASSO 7: Testar o Site

Você deve ver:
- ✅ Página inicial com os testes
- ✅ Botão para começar o teste
- ✅ Tudo funcionar normalmente

Se vir erro **502 Bad Gateway** ou página branca:
- Aguarde mais 1 minuto
- Atualize a página (Ctrl+F5 para limpar cache)
- Se persistir, vá para PASSO 3 novamente

---

## PASSO 8: Verificar se o Deploy Realmente Funcionou

Faça um teste rápido:
1. Abra a URL do seu site
2. Clique em um teste (ex: "Descubra seu Signo")
3. Responda as perguntas
4. Clique em "Enviar"
5. Você deve ver o resultado

Se tudo aparecer, está funcionando! 🎉

---

## 🆘 AINDA NÃO FUNCIONA?

### Opção 1: Forçar Redeploy

1. Vá em **"Deployments"**
2. Clique no último deploy (com ✓)
3. Clique em **"Redeploy"**
4. Aguarde novamente

### Opção 2: Verificar o Código

Voltando ao seu computador:

```bash
# Verificar se o código tem erros
python manage.py check

# Se tiver erro, corrija
# Depois faça push novamente
git add .
git commit -m "Corrigir erro"
git push origin master
```

### Opção 3: Limpar Tudo e Começar do Zero

No Railway Dashboard:
1. Clique em **"Settings"** (engrenagem)
2. Desça até o final
3. Clique em **"Delete Environment"** (ou similar)
4. Crie um novo deployment

---

## 📋 CHECKLIST FINAL

Antes de desistir, verifique:

- [ ] Você fez `git push origin master` com sucesso?
- [ ] A URL do GitHub mostra seus últimos commits?
- [ ] No Railway, você vê um deploy verde/sucesso?
- [ ] Você adicionou `DEBUG=False` nas variáveis?
- [ ] Você adicionou `SECRET_KEY` nas variáveis?
- [ ] Você adicionou `PYTHONUNBUFFERED=1` nas variáveis?
- [ ] Você aguardou 2-3 minutos após adicionar variáveis?
- [ ] Você abriu a URL em uma **aba nova** (não no mesmo navegador)?

---

## 📞 Precisa de Ajuda?

Se nada disso funcionar:

1. **Copie TODO o texto do log de erro** do Railway
2. **Descreva o que fez** (push, addvariáveis, etc)
3. **Abra uma issue** no repositório GitHub
4. **Ou me mande uma screenshot** dos logs

Boa sorte! 🚀

---

**Última atualização:** 24/11/2025
