@echo off
chcp 65001 >nul
echo.
echo ═══════════════════════════════════════════════════════════════
echo     🚀 SCRIPT DE DEPLOY - GITHUB + RAILWAY
echo ═══════════════════════════════════════════════════════════════
echo.

:menu
echo.
echo Escolha uma opção:
echo.
echo [1] Ver status do Git
echo [2] Conectar ao GitHub (primeira vez)
echo [3] Enviar mudanças para o GitHub
echo [4] Ver commits recentes
echo [5] Abrir GitHub no navegador
echo [6] Abrir Railway no navegador
echo [0] Sair
echo.
set /p opcao="Digite o número: "

if "%opcao%"=="1" goto status
if "%opcao%"=="2" goto conectar
if "%opcao%"=="3" goto push
if "%opcao%"=="4" goto log
if "%opcao%"=="5" goto github
if "%opcao%"=="6" goto railway
if "%opcao%"=="0" goto fim
goto menu

:status
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
git status
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pause
goto menu

:conectar
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 📝 PRIMEIRO, CRIE O REPOSITÓRIO NO GITHUB:
echo.
echo 1. Acesse: https://github.com/new
echo 2. Nome: testes-perfil
echo 3. Public ou Private
echo 4. NÃO marque nenhuma opção adicional
echo 5. Clique em "Create repository"
echo 6. COPIE a URL que aparecer
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
set /p url="Cole a URL do repositório aqui: "
echo.
echo 🔗 Conectando ao GitHub...
git remote add origin %url%
git branch -M main
echo.
echo ✅ Pronto! Agora escolha a opção [3] para enviar o código.
echo.
pause
goto menu

:push
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 📤 Enviando código para o GitHub...
echo.
git push -u origin main
echo.
if %errorlevel% equ 0 (
    echo ✅ Código enviado com sucesso!
    echo.
    echo 🎉 PRÓXIMO PASSO: Deploy no Railway
    echo    Abra: https://railway.app/
    echo    Clique em "New Project" -^> "Deploy from GitHub repo"
) else (
    echo ❌ Erro ao enviar. Possíveis causas:
    echo    - Não configurou o remote (use opção 2)
    echo    - Precisa de autenticação (use Personal Access Token)
    echo.
    echo 💡 Precisa de Personal Access Token?
    echo    1. github.com -^> Settings -^> Developer settings
    echo    2. Personal access tokens -^> Generate new token
    echo    3. Marque "repo"
    echo    4. Copie o token e use como senha
)
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pause
goto menu

:log
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
git log --oneline -10
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pause
goto menu

:github
echo.
echo 🌐 Abrindo GitHub...
start https://github.com/new
goto menu

:railway
echo.
echo 🚂 Abrindo Railway...
start https://railway.app/
goto menu

:fim
echo.
echo 👋 Até logo!
echo.
exit

