@echo off
REM Script para backup do banco de dados SQLite no Railway (Windows)

echo 🔄 Fazendo backup do banco de dados...

REM Data atual
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c%%a%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
set BACKUP_FILE=backup_%mydate%_%mytime%.json

REM Fazer dump dos dados
python manage.py dumpdata --indent 2 --exclude auth.permission --exclude contenttypes > %BACKUP_FILE%

echo ✅ Backup criado: %BACKUP_FILE%
echo.
echo 💡 Para restaurar este backup:
echo    python manage.py loaddata %BACKUP_FILE%
pause
