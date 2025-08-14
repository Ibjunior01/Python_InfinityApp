import flet as ft
from services.gerenciador import GerenciadorDeReservas
from models.cliente import Cliente
from models.quarto import Quarto

from ui.tela_inicial import tela_inicial
from ui.formulario_reserva import formulario_reserva
from ui.gerenciamento_clientes import gerenciamento_clientes
from ui.visualizacao_reservas import visualizacao_reservas

gerenciador = GerenciadorDeReservas()

# Dados iniciais
gerenciador.adicionar_cliente(Cliente("Ibermon", "99999-9999", "ibermon@email.com", "C001"))
gerenciador.adicionar_quarto(Quarto(101, "single", 200))
gerenciador.adicionar_quarto(Quarto(102, "double", 350))

def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos"

    # Atualizado para NavigationBarDestination
    page.navigation_bar = ft.NavigationBar(
    destinations=[
        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
        ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="Reservar"),
        ft.NavigationBarDestination(icon=ft.Icons.PERSON_ADD, label="Clientes"),
        ft.NavigationBarDestination(icon=ft.Icons.LIST, label="Reservas"),
    ]
)

    def navegar(e):
        page.controls.clear()
        index = e.control.selected_index
        page.navigation_bar.selected_index = index

        if index == 0:
            tela_inicial(page, gerenciador)
        elif index == 1:
            formulario_reserva(page, gerenciador)
        elif index == 2:
            gerenciamento_clientes(page, gerenciador)
        elif index == 3:
            visualizacao_reservas(page, gerenciador)

        page.update()

    page.navigation_bar.on_change = navegar

    # Tela inicial padrão
    tela_inicial(page, gerenciador)

ft.app(target=main)