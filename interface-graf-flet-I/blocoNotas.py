import flet as ft

def main(page: ft.Page):
    page.title = "Bloco de Notas"

    texto = ft.TextField(multiline=True, min_lines=10, expand=True)
    status = ft.Text()

    def salvar(e):
        with open("notas.txt", "w", encoding="utf-8") as f:
            f.write(texto.value)
        status.value = "Texto salvo em notas.txt"
        page.update()

    botao_salvar = ft.ElevatedButton(text="Salvar", on_click=salvar)

    page.add(texto, botao_salvar, status)

ft.app(target=main)