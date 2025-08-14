class Pedido:
    def __init__(self, descricao, cliente):
        self.descricao = descricao
        self.cliente = cliente
        cliente.adicionar_pedido(self)

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        print(f"Pedidos de {self.nome}:")
        for pedido in self.pedidos:
            print(f"- {pedido.descricao}")

# Exemplo de uso
cliente = Cliente("Ibermon")
Pedido("Notebook", cliente)
Pedido("Mouse Gamer", cliente)
cliente.listar_pedidos()