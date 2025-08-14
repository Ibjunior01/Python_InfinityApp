import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
SELECT v.nome_vendedor, vd.valor
FROM vendedores v
LEFT JOIN vendas vd ON v.vendedor_id = vd.vendedor_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()