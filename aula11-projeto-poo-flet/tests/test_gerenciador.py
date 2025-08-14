import unittest
from services.gerenciador import GerenciadorDeReservas
from models.cliente import Cliente
from models.quarto import Quarto

class TestGerenciadorDeReservas(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorDeReservas()
        self.cliente = Cliente("Teste", "0000-0000", "teste@email.com", "T001")
        self.quarto = Quarto(201, "suite", 500)
        self.gerenciador.adicionar_cliente(self.cliente)
        self.gerenciador.adicionar_quarto(self.quarto)

    def test_adicionar_cliente(self):
        self.assertEqual(len(self.gerenciador.clientes), 1)
        self.assertEqual(self.gerenciador.clientes[0].get_nome(), "Teste")

    def test_adicionar_quarto(self):
        self.assertEqual(len(self.gerenciador.quartos), 1)
        self.assertTrue(self.quarto.esta_disponivel())

    def test_criar_reserva(self):
        reserva = self.gerenciador.criar_reserva("T001", 201, "01/09/2025", "05/09/2025")
        self.assertIsNotNone(reserva)
        self.assertEqual(reserva.cliente.get_id(), "T001")
        self.assertFalse(self.quarto.esta_disponivel())

    def test_reserva_invalida(self):
        reserva = self.gerenciador.criar_reserva("X999", 999, "01/09/2025", "05/09/2025")
        self.assertIsNone(reserva)

if __name__ == "__main__":
    unittest.main()