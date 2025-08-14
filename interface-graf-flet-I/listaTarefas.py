import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"

    entrada = ft.TextField(label="Nova tarefa", width=300)
    lista = ft.ListView(expand=True, spacing=10, padding=10)

    def adicionar_tarefa(e):
        if entrada.value:
            tarefa = ft.Checkbox(label=entrada.value)
            lista.controls.append(tarefa)
            entrada.value = ""
            page.update()

    botao = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)

    page.add(entrada, botao, lista)

ft.app(target=main)