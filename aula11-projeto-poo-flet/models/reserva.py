class Reserva:
    def __init__(self, cliente, quarto, checkin, checkout):
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.status = "Ativa"

    def cancelar(self):
        self.status = "Cancelada"
        self.quarto.set_disponibilidade(True)

    def exibir_resumo(self):
        return f"{self.cliente.get_nome()} reservou o quarto {self.quarto.get_numero()} de {self.checkin} a {self.checkout} - Status: {self.status}"