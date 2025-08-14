# src/test_desafio2.py
from src.db import get_conn

def criar_tabela():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY,
        NomeProduto TEXT NOT NULL,
        Quantidade INTEGER NOT NULL,
        Preco REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def inserir_dados():
    conn = get_conn()
    cur = conn.cursor()

    produtos = [
        (1, "Notebook", 10, 2500.00),
        (2, "Mouse Gamer", 50, 150.00),
        (3, "Teclado Mecânico", 30, 350.00)
    ]

    cur.executemany("INSERT INTO Produtos VALUES (?, ?, ?, ?)", produtos)
    conn.commit()
    conn.close()

def listar_produtos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Produtos")
    for row in cur.fetchall():
        print(row)
    conn.close()

if __name__ == "__main__":
    criar_tabela()
    inserir_dados()
    listar_produtos()
