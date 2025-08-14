# consultas/clientes_pedidos.py
import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
SELECT c.nome_cliente, p.numero_pedido
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()