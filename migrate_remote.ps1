# Script para rodar migrações Django contra um banco de dados remoto
# Uso: .\migrate_remote.ps1 -DatabaseUrl "postgres://user:pass@host:5432/dbname"

param(
    [Parameter(Mandatory=$true)]
    [string]$DatabaseUrl,
    
    [Parameter(Mandatory=$false)]
    [string]$App = "",
    
    [Parameter(Mandatory=$false)]
    [switch]$ShowSQL = $false
)

# Determinar o diretório do script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Verificar se o venv existe
if (-not (Test-Path ".\venv\Scripts\python.exe")) {
    Write-Error "Virtual environment não encontrado em .\venv\Scripts\python.exe"
    exit 1
}

Write-Host "🔄 Rodando migrations com DATABASE_URL remoto..." -ForegroundColor Cyan
Write-Host "📍 Banco: $($DatabaseUrl.Split('@')[1] -replace '.*/', '')" -ForegroundColor Yellow

# Construir comando
$pythonExe = ".\venv\Scripts\python.exe"
$command = @($pythonExe, "manage.py", "migrate")

if ($App) {
    $command += $App
}

if ($ShowSQL) {
    $command += "--verbosity=3"
} else {
    $command += "--verbosity=2"
}

# Rodar com a DATABASE_URL
$env:DATABASE_URL = $DatabaseUrl
& $pythonExe @($command -split '\s+') | Where-Object { $_ }

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Migrações executadas com sucesso!" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao executar migrações (código $LASTEXITCODE)" -ForegroundColor Red
    exit 1
}
