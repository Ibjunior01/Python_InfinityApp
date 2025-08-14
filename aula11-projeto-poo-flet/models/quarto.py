class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco_diaria = preco_diaria
        self.__disponivel = True

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_preco_diaria(self):
        return self.__preco_diaria

    def esta_disponivel(self):
        return self.__disponivel

    def set_disponibilidade(self, status):
        self.__disponivel = status