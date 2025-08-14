import flet as ft

def formulario_reserva(page, gerenciador):
    cliente_id = ft.TextField(label="ID do Cliente")
    numero_quarto = ft.TextField(label="Número do Quarto")
    checkin = ft.TextField(label="Data de Check-in (dd/mm/aaaa)")
    checkout = ft.TextField(label="Data de Check-out (dd/mm/aaaa)")
    resultado = ft.Text()

    def reservar(e):
        reserva = gerenciador.criar_reserva(
            cliente_id.value,
            int(numero_quarto.value),
            checkin.value,
            checkout.value
        )
        if reserva:
            resultado.value = "Reserva criada com sucesso!"
        else:
            resultado.value = "Erro ao criar reserva. Verifique os dados."
        page.update()

    page.add(
        ft.Text("Formulário de Reserva", size=20, weight="bold"),
        cliente_id,
        numero_quarto,
        checkin,
        checkout,
        ft.ElevatedButton(text="Reservar", on_click=reservar),
        resultado
    )