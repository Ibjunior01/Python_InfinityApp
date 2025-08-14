from db import get_conn
import pandas as pd

# Inserir alguns registros
with get_conn() as conn:
    conn.execute("INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)", ("João", 30, "São Paulo"))
    conn.execute("INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)", ("Maria", 25, "Rio de Janeiro"))
    conn.execute("INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)", ("Pedro", 40, "Belo Horizonte"))
    conn.commit()

# Consultar e mostrar
with get_conn() as conn:
    df = pd.read_sql("SELECT * FROM Clientes", conn)
    print("\nLista de clientes:")
    print(df.to_string(index=False))
