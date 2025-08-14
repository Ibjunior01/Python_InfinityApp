import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
SELECT p.nome, d.tipo
FROM pessoas p
LEFT JOIN documentos d ON p.pessoa_id = d.pessoa_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()