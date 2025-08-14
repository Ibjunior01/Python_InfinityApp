import flet as ft
from models.cliente import Cliente

def gerenciamento_clientes(page, gerenciador):
    nome = ft.TextField(label="Nome")
    telefone = ft.TextField(label="Telefone")
    email = ft.TextField(label="Email")
    id_cliente = ft.TextField(label="ID do Cliente")
    resultado = ft.Text()

    def cadastrar(e):
        cliente = Cliente(nome.value, telefone.value, email.value, id_cliente.value)
        gerenciador.adicionar_cliente(cliente)
        resultado.value = f"Cliente {nome.value} cadastrado com sucesso!"
        page.update()

    page.add(
        ft.Text("Cadastro de Clientes", size=20, weight="bold"),
        nome,
        telefone,
        email,
        id_cliente,
        ft.ElevatedButton(text="Cadastrar", on_click=cadastrar),
        resultado
    )