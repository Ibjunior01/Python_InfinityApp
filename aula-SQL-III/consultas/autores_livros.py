import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
SELECT a.nome_autor, l.titulo
FROM autores a
LEFT JOIN livros l ON a.autor_id = l.autor_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()