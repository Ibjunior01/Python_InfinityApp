import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
SELECT l.titulo, e.nome_editora
FROM livros l
LEFT JOIN livros_editora le ON l.livro_id = le.livro_id
LEFT JOIN editoras e ON le.editora_id = e.editora_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()