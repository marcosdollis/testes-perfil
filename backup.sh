#!/bin/bash
# Script para backup do banco de dados SQLite no Railway

echo "🔄 Fazendo backup do banco de dados..."

# Data atual
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="backup_${DATE}.json"

# Fazer dump dos dados
python manage.py dumpdata --indent 2 --exclude auth.permission --exclude contenttypes > $BACKUP_FILE

echo "✅ Backup criado: $BACKUP_FILE"
echo ""
echo "📊 Estatísticas do backup:"
echo "   - Tamanho: $(du -h $BACKUP_FILE | cut -f1)"
echo "   - Data: $(date)"
echo ""
echo "💡 Para restaurar este backup:"
echo "   python manage.py loaddata $BACKUP_FILE"
