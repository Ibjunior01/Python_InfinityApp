from database.conexao import conectar
from models.venda import Venda

def registrar_venda(venda):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vendas (produto_id, quantidade, data_venda) VALUES (%s, %s, %s)",
        (venda.produto_id, venda.quantidade, venda.data_venda)
    )
    cursor.execute(
        "UPDATE produtos SET quantidade = quantidade - %s WHERE id = %s",
        (venda.quantidade, venda.produto_id)
    )
    conn.commit()
    conn.close()