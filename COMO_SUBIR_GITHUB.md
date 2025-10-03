# 📦 GUIA: CRIAR REPOSITÓRIO NO GITHUB

## ✅ Git Local JÁ CONFIGURADO!

Seu projeto já está pronto localmente:
- ✅ Git inicializado
- ✅ 31 arquivos commitados
- ✅ Pronto para subir ao GitHub

---

## 🚀 PRÓXIMOS PASSOS:

### 1️⃣ **CRIAR REPOSITÓRIO NO GITHUB**

#### Opção A: Via Site (RECOMENDADO para iniciantes)

1. Acesse: https://github.com/new

2. Preencha:
   ```
   Repository name: testes-perfil
   Description: Plataforma de testes psicológicos (QI, Personalidade, Renda) com paywall de R$ 4,99
   
   ☑️ Public (ou Private se preferir)
   ❌ NÃO marque "Add a README file"
   ❌ NÃO marque "Add .gitignore"
   ❌ NÃO marque "Choose a license"
   ```

3. Clique em **"Create repository"**

4. **COPIE a URL** que aparecer (será algo como):
   ```
   https://github.com/SEU_USUARIO/testes-perfil.git
   ```

---

### 2️⃣ **CONECTAR SEU PROJETO AO GITHUB**

Volte aqui no VS Code e execute estes comandos:

```powershell
# Conectar ao repositório do GitHub
git remote add origin https://github.com/SEU_USUARIO/testes-perfil.git

# Renomear branch para 'main'
git branch -M main

# Enviar para o GitHub
git push -u origin main
```

**⚠️ IMPORTANTE:** Substitua `SEU_USUARIO` pelo seu usuário do GitHub!

---

### 3️⃣ **AUTENTICAÇÃO (se pedir senha)**

O GitHub não aceita mais senha. Use **Personal Access Token**:

#### Como criar Token:

1. GitHub → Clique na sua foto (canto superior direito)
2. Settings → Developer settings (no final da página)
3. Personal access tokens → Tokens (classic)
4. "Generate new token (classic)"
5. Marque: `repo` (dá acesso completo aos repositórios)
6. Clique em "Generate token"
7. **COPIE O TOKEN** (você não verá novamente!)

#### Quando pedir senha:
```
Username: seu_usuario_github
Password: cole_o_token_aqui
```

---

## 📋 COMANDOS PRONTOS PARA VOCÊ:

Depois de criar o repo no GitHub, copie e cole TUDO de uma vez:

```powershell
cd "c:\Users\Marcos\Documents\python projects\testes-perfil"
git remote add origin https://github.com/SEU_USUARIO/testes-perfil.git
git branch -M main
git push -u origin main
```

**🎉 Depois disso, seu código estará no GitHub!**

---

## 🔄 COMANDOS ÚTEIS PARA O FUTURO:

### Fazer mudanças e enviar:
```powershell
git add .
git commit -m "Descrição da mudança"
git push
```

### Ver status:
```powershell
git status
```

### Ver histórico:
```powershell
git log --oneline
```

### Criar nova branch:
```powershell
git checkout -b nova-funcionalidade
```

---

## 🚀 DEPOIS QUE SUBIR PARA O GITHUB:

### **Deploy no Railway:**

1. Vá em: https://railway.app/
2. Login com GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecione: `testes-perfil`
5. Configure as variáveis (arquivo `RAILWAY_ENV_VARS.txt`)
6. Crie volume: `/app/data`
7. Deploy automático! 🎉

---

## ⚠️ PROBLEMAS COMUNS:

### "Authentication failed"
→ Use Personal Access Token ao invés de senha

### "Repository not found"
→ Verifique se a URL está correta
→ Certifique-se de que você criou o repositório

### "Updates were rejected"
→ Execute: `git pull origin main --rebase`
→ Depois: `git push`

---

## 📞 PRECISA DE AJUDA?

1. Me avise qual erro apareceu
2. Copie e cole a mensagem de erro completa
3. Te ajudo a resolver!

---

**Pronto! Siga os passos acima e me avise quando criar o repositório no GitHub!** 🚀
