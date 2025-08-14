from models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id_cliente):
        super().__init__(nome, telefone, email)
        self.__id_cliente = id_cliente

    def get_id(self):
        return self.__id_cliente

    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()}, ID: {self.__id_cliente}"