import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Listar tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("=" * 50)
print("TABELAS NO BANCO DE DADOS:")
print("=" * 50)
for table in tables:
    print(f"  📊 {table[0]}")
    
    # Contar registros em cada tabela
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
        count = cursor.fetchone()[0]
        print(f"      └─ {count} registros")
    except:
        pass

print("\n" + "=" * 50)
print("VERIFICANDO SE O BANCO ESTÁ SENDO USADO:")
print("=" * 50)

# Verificar sessões
cursor.execute("SELECT COUNT(*) FROM django_session")
sessions_count = cursor.fetchone()[0]
print(f"  🔑 Sessões ativas: {sessions_count}")

# Verificar se há dados nas tabelas do app
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'testes_%'")
app_tables = cursor.fetchall()

if app_tables:
    print(f"\n  📁 Tabelas do app 'testes': {len(app_tables)}")
    for table in app_tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
        count = cursor.fetchone()[0]
        print(f"      └─ {table[0]}: {count} registros")
else:
    print(f"\n  ⚠️  Nenhuma tabela do app 'testes' encontrada")

print("\n" + "=" * 50)
print("RESUMO:")
print("=" * 50)
if sessions_count > 0:
    print("  ✅ O banco ESTÁ sendo usado (há sessões ativas)")
    print("  💾 Os dados dos testes estão sendo salvos nas sessões")
else:
    print("  ⚠️  Nenhuma sessão ativa no momento")

print("\n  ℹ️  IMPORTANTE:")
print("  └─ Este projeto usa SESSÕES para armazenar resultados")
print("  └─ NÃO usa models/tabelas para os testes")
print("  └─ Banco só tem tabelas padrão do Django (admin, auth, sessions)")

conn.close()
