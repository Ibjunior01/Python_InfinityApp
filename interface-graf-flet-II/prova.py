# Formulário de contatos com estilização e tema.

import flet as ft

def main(page: ft.Page):
    # Tema com uso de valores hexadecimais
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#2196F3",                     secondary="#FFC107",       
            background="#F5F5F5",      
            on_primary="#FFFFFF",                on_secondary="#000000"          )
    )
    page.bgcolor = page.theme.color_scheme.background
    page.title = "Formulário de Contato"

    # Campos de entrada (sem parâmetros inválidos)
    nome = ft.TextField(
        label="Nome",
        width=400,
        text_style=ft.TextStyle(size=16)
    )

    email = ft.TextField(
        label="Email",
        width=400,
        text_style=ft.TextStyle(size=16)
    )

    mensagem = ft.TextField(
        label="Mensagem",
        multiline=True,
        min_lines=4,
        width=400,
        text_style=ft.TextStyle(size=16)
    )

    # Mensagem de confirmação
    confirmacao = ft.Text(value="", color="#43A047", weight="bold")  

    # Botão de envio
    def enviar(e):
        if nome.value and email.value and mensagem.value:
            confirmacao.value = f"Obrigado, {nome.value}! Sua mensagem foi enviada com sucesso."
        else:
            confirmacao.value = "Por favor, preencha todos os campos."
        page.update()

    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        bgcolor=page.theme.color_scheme.primary,
        color=page.theme.color_scheme.on_primary,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=10
        ),
        on_click=enviar
    )

    # Layout da página
    page.add(
        ft.Text("Formulário de Contato", size=24, weight="bold", color="#1976D2"),  
        nome,
        email,
        mensagem,
        botao_enviar,
        confirmacao
    )

ft.app(target=main)