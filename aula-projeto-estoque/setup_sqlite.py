import sqlite3

conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    descricao TEXT,
    quantidade INTEGER,
    preco REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    quantidade INTEGER,
    data_venda TEXT,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
""")

conn.commit()
conn.close()

print("Banco de dados e tabelas criados com sucesso!")