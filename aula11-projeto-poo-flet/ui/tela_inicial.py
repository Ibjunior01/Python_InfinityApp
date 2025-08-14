import flet as ft

def tela_inicial(page, gerenciador):
    lista_quartos = ft.Column()
    lista_reservas = ft.Column()

    def atualizar():
        lista_quartos.controls.clear()
        for q in gerenciador.listar_quartos_disponiveis():
            lista_quartos.controls.append(ft.Text(f"Quarto {q.get_numero()} - {q.get_tipo()} - R${q.get_preco_diaria():.2f}"))
        lista_reservas.controls.clear()
        for r in gerenciador.listar_reservas():
            lista_reservas.controls.append(ft.Text(r.exibir_resumo()))
        page.update()

    page.add(
        ft.Text("Quartos Disponíveis", size=20, weight="bold"),
        lista_quartos,
        ft.Text("Reservas Ativas", size=20, weight="bold"),
        lista_reservas,
        ft.ElevatedButton(text="Atualizar", on_click=lambda e: atualizar())
    )

    atualizar()