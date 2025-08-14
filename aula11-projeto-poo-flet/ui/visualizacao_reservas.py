import flet as ft

def visualizacao_reservas(page, gerenciador):
    lista = ft.Column()

    def atualizar():
        lista.controls.clear()
        for r in gerenciador.listar_reservas():
            lista.controls.append(ft.Text(r.exibir_resumo()))
        page.update()

    page.add(
        ft.Text("Reservas Ativas", size=20, weight="bold"),
        lista,
        ft.ElevatedButton(text="Atualizar", on_click=lambda e: atualizar())
    )

    atualizar()