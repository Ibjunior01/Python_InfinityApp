from models.reserva import Reserva

class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def listar_quartos_disponiveis(self):
        return [q for q in self.quartos if q.esta_disponivel()]

    def criar_reserva(self, cliente_id, numero_quarto, checkin, checkout):
        cliente = next((c for c in self.clientes if c.get_id() == cliente_id), None)
        quarto = next((q for q in self.quartos if q.get_numero() == numero_quarto and q.esta_disponivel()), None)
        if cliente and quarto:
            reserva = Reserva(cliente, quarto, checkin, checkout)
            quarto.set_disponibilidade(False)
            self.reservas.append(reserva)
            return reserva
        return None

    def listar_reservas(self):
        return self.reservas