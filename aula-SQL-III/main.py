import os

consultas = [
    "clientes_pedidos",
    "vendedores_vendas",
    "pessoas_documentos",
    "autores_livros",
    "musicos_bandas",
    "biblioteca",
    "estoque"
]

for consulta in consultas:
    print(f"\nExecutando: {consulta}")
    os.system(f"python consultas/{consulta}.py")