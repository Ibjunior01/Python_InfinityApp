class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = max(0, preco)
        self._quantidade = max(0, quantidade)

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self._preco = novo_preco

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, nova_qtd):
        if nova_qtd >= 0:
            self._quantidade = nova_qtd

# Exemplo de uso
produto = Produto("Teclado", 150, 10)
produto.set_preco(-50)  # Ignorado
print(produto.get_preco())  