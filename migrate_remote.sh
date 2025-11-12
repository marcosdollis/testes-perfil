#!/bin/bash
# Script para rodar migrações Django contra um banco de dados remoto
# Uso: ./migrate_remote.sh "postgres://user:pass@host:5432/dbname"

if [ -z "$1" ]; then
    echo "❌ Erro: DATABASE_URL é obrigatório"
    echo "Uso: $0 <DATABASE_URL> [app_name] [--verbose]"
    echo ""
    echo "Exemplo:"
    echo "  $0 'postgres://user:pass@railway.app:5432/railway' testes"
    exit 1
fi

DATABASE_URL="$1"
APP="${2:-}"
VERBOSE="${3:-}"

# Determinar diretório do script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Verificar se o venv existe
if [ ! -f "./venv/bin/python" ]; then
    echo "❌ Virtual environment não encontrado em ./venv/bin/python"
    exit 1
fi

echo "🔄 Rodando migrations com DATABASE_URL remoto..."
echo "📍 Banco: $(echo $DATABASE_URL | sed 's/.*@//')"

# Rodar migrações
export DATABASE_URL="$DATABASE_URL"

PYTHON_BIN="./venv/bin/python"
CMD="$PYTHON_BIN manage.py migrate"

if [ ! -z "$APP" ]; then
    CMD="$CMD $APP"
fi

if [ "$VERBOSE" = "--verbose" ] || [ "$VERBOSE" = "-v" ]; then
    CMD="$CMD --verbosity=3"
else
    CMD="$CMD --verbosity=2"
fi

echo "Executando: $CMD"
$CMD

if [ $? -eq 0 ]; then
    echo "✅ Migrações executadas com sucesso!"
else
    echo "❌ Erro ao executar migrações"
    exit 1
fi
