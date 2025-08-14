# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from models.produto import Produto
# from models.venda import Venda
# from services.produto_service import cadastrar_produto, listar_produtos, atualizar_estoque, remover_produto
# from services.venda_service import registrar_venda

# # Exemplo de uso
# produto = Produto("Mouse Gamer", "Mouse RGB com 6 botões", 50, 129.90)
# cadastrar_produto(produto)

# for p in listar_produtos():
#     print(p)

# atualizar_estoque(1, 45)
# remover_produto(2)

# venda = Venda(produto_id=1, quantidade=2)
# registrar_venda(venda)
from models.produto import Produto
from services.produto_service import cadastrar_produto, listar_produtos

produto = Produto("Teclado Mecânico", "Switch azul, RGB", 20, 199.90)
cadastrar_produto(produto)

for p in listar_produtos():
    print(p)