import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Cadastro"

    nome = ft.TextField(label="Nome")
    sobrenome = ft.TextField(label="Sobrenome")
    email = ft.TextField(label="Email")
    resultado = ft.Text()

    def cadastrar(e):
        resultado.value = f"Cadastro realizado: {nome.value} {sobrenome.value} ({email.value})"
        page.update()

    botao = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar)

    page.add(nome, sobrenome, email, botao, resultado)

ft.app(target=main)