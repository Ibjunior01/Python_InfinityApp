#Aplicativo de Lista de Tarefas Dinâmica
import flet as ft

def main(page: ft.Page):
    page.title = "Tarefas Dinâmicas"

    entrada = ft.TextField(label="Digite uma tarefa", width=300)
    lista = ft.Column()

    def adicionar(e):
        if entrada.value:
            item = ft.Text(entrada.value)
            lista.controls.append(item)
            entrada.value = ""
            page.update()

    botao = ft.ElevatedButton(text="Adicionar Tarefa", on_click=adicionar)

    page.add(entrada, botao, lista)

ft.app(target=main)