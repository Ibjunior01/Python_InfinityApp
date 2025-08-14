from database.conexao import conectar
from models.produto import Produto

def cadastrar_produto(produto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao, quantidade, preco) VALUES (?, ?, ?, ?)",
        (produto.nome, produto.descricao, produto.quantidade, produto.preco)
    )
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def atualizar_estoque(id_produto, nova_quantidade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))
    conn.commit()
    conn.close()

def remover_produto(id_produto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conn.commit()
    conn.close()