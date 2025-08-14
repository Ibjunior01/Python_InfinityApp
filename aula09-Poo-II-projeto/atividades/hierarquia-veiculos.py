class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None

    def set_cor(self, cor):
        self.cor = cor
        return self

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self

class Carro(Veiculo):
    pass

class Bicicleta(Veiculo):
    pass