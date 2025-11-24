#!/bin/bash
# Script para verificar se a aplicação Django está pronta para deploy

echo "🔍 Verificando aplicação Django..."
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0
WARNINGS=0

# 1. Verificar requirements.txt
echo "📦 Verificando requirements.txt..."
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}✓${NC} requirements.txt encontrado"
    
    # Verificar dependências críticas
    DEPS=("Django" "daphne" "channels" "whitenoise" "psycopg2-binary")
    for dep in "${DEPS[@]}"; do
        if grep -q "$dep" requirements.txt; then
            echo -e "  ${GREEN}✓${NC} $dep encontrado"
        else
            echo -e "  ${YELLOW}⚠${NC} $dep NÃO encontrado"
            WARNINGS=$((WARNINGS + 1))
        fi
    done
else
    echo -e "${RED}✗${NC} requirements.txt não encontrado"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 2. Verificar Procfile
echo "🚀 Verificando Procfile..."
if [ -f "Procfile" ]; then
    echo -e "${GREEN}✓${NC} Procfile encontrado"
    cat Procfile
else
    echo -e "${RED}✗${NC} Procfile não encontrado"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 3. Verificar railway.json
echo "🚂 Verificando railway.json..."
if [ -f "railway.json" ]; then
    echo -e "${GREEN}✓${NC} railway.json encontrado"
else
    echo -e "${RED}✗${NC} railway.json não encontrado"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 4. Verificar manage.py
echo "⚙️ Verificando manage.py..."
if [ -f "manage.py" ]; then
    echo -e "${GREEN}✓${NC} manage.py encontrado"
else
    echo -e "${RED}✗${NC} manage.py não encontrado"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 5. Verificar pasta templates
echo "📄 Verificando templates..."
if [ -d "templates" ]; then
    echo -e "${GREEN}✓${NC} Pasta templates encontrada"
    TEMPLATE_COUNT=$(find templates -name "*.html" | wc -l)
    echo "  Encontrados: $TEMPLATE_COUNT arquivos HTML"
else
    echo -e "${RED}✗${NC} Pasta templates não encontrada"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# 6. Verificar pasta static (se necessário)
echo "🎨 Verificando static files..."
if [ -d "static" ]; then
    echo -e "${GREEN}✓${NC} Pasta static encontrada"
else
    echo -e "${YELLOW}⚠${NC} Pasta static não encontrada (pode ser criada automaticamente)"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# 7. Resumo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 RESUMO:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "Erros: ${RED}$ERRORS${NC}"
echo -e "Avisos: ${YELLOW}$WARNINGS${NC}"
echo ""

if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✓ Aplicação pronta para deploy!${NC}"
    exit 0
else
    echo -e "${RED}✗ Corrija os erros acima antes de fazer deploy${NC}"
    exit 1
fi
