from db import get_conn
import pandas as pd

# 1) Inserir dados no Desafio 02
with get_conn() as conn:
    conn.execute("INSERT INTO produtos_teste (NomeProduto, Quantidade, Preco) VALUES (?, ?, ?)", ("Mouse Gamer", 15, 120.50))
    conn.execute("INSERT INTO produtos_teste (NomeProduto, Quantidade, Preco) VALUES (?, ?, ?)", ("Teclado Mecânico", 8, 250.00))
    conn.execute("INSERT INTO produtos_teste (NomeProduto, Quantidade, Preco) VALUES (?, ?, ?)", ("Monitor 24\"", 5, 900.00))
    conn.commit()

# 2) Consultar e exibir
with get_conn() as conn:
    df = pd.read_sql("SELECT * FROM produtos_teste", conn)
    print("\nProdutos cadastrados:")
    print(df.to_string(index=False))

# 3) Exemplo de consulta de clientes (Desafio 01)
with get_conn() as conn:
    df_clientes = pd.read_sql("SELECT * FROM clientes_loja", conn)
    print("\nClientes cadastrados na loja:")
    print(df_clientes.to_string(index=False))
