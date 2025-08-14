import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
SELECT m.nome_musico, b.nome_banda
FROM musicos m
LEFT JOIN musicos_bandas mb ON m.musico_id = mb.musico_id
LEFT JOIN bandas b ON mb.banda_id = b.banda_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()