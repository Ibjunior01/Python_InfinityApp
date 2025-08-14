import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Tabela de produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    produto_id INTEGER PRIMARY KEY,
    nome_produto TEXT
)
""")

# Tabela de fornecedores
cursor.execute("""
CREATE TABLE IF NOT EXISTS fornecedores (
    fornecedor_id INTEGER PRIMARY KEY,
    nome_fornecedor TEXT
)
""")

# Apagar a tabela estoque se já existir
cursor.execute("DROP TABLE IF EXISTS estoque")

# Tabela de estoque com chaves estrangeiras
cursor.execute("""
CREATE TABLE estoque (
    estoque_id INTEGER PRIMARY KEY,
    produto_id INTEGER,
    fornecedor_id INTEGER,
    quantidade INTEGER,
    data_entrada TEXT,
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(fornecedor_id)
)
""")


# Inserir produtos
cursor.executemany("""
INSERT INTO produtos (nome_produto) VALUES (?)
""", [("Caderno",), ("Caneta",), ("Borracha",)])

# Inserir fornecedores
cursor.executemany("""
INSERT INTO fornecedores (nome_fornecedor) VALUES (?)
""", [("Fornecedor A",), ("Fornecedor B",)])

# Inserir entradas no estoque
cursor.executemany("""
INSERT INTO estoque (produto_id, fornecedor_id, quantidade, data_entrada)
VALUES (?, ?, ?, ?)
""", [
    (1, 1, 100, "2025-08-01"),
    (2, 2, 200, "2025-08-02"),
    (3, 1, 150, "2025-08-03")
])

# Simulação de FULL OUTER JOIN entre produtos e estoque
cursor.execute("""
SELECT p.nome_produto, e.quantidade, e.data_entrada
FROM produtos p
LEFT JOIN estoque e ON p.produto_id = e.produto_id

UNION

SELECT p.nome_produto, e.quantidade, e.data_entrada
FROM estoque e
LEFT JOIN produtos p ON p.produto_id = e.produto_id
""")

print(" FULL OUTER JOIN (simulado):")
for row in cursor.fetchall():
    print(row)

    # Agrupar por fornecedor e somar quantidade
cursor.execute("""
SELECT f.nome_fornecedor, SUM(e.quantidade) AS total_recebido
FROM fornecedores f
JOIN estoque e ON f.fornecedor_id = e.fornecedor_id
GROUP BY f.nome_fornecedor
""")

print("\n Quantidade total por fornecedor:")
for row in cursor.fetchall():
    print(row)

    # Adicionar uma nova coluna: observacao
cursor.execute("""
ALTER TABLE estoque ADD COLUMN observacao TEXT
""")

print("\n Coluna 'observacao' adicionada à tabela estoque.")

conn.commit()
conn.close()