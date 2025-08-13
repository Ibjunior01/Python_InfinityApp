class Hotel:
    def __init__(self):
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def adicionar_funcionario(self, nome, funcao, salario):
        self.funcionarios.append({'nome': nome, 'funcao': funcao, 'salario': salario})

    def adicionar_quarto(self, numero, diaria):
        self.quartos.append({'numero': numero, 'diaria': diaria, 'status': 'disponível'})

    def reservar_quarto(self, hospede, dias, numero_quarto):
        for quarto in self.quartos:
            if quarto['numero'] == numero_quarto and quarto['status'] == 'disponível':
                quarto['status'] = 'ocupado'
                self.reservas.append({'hospede': hospede, 'dias': dias, 'quarto': numero_quarto})
                return
        print("Quarto indisponível.")

    def calcular_conta(self, hospede):
        for reserva in self.reservas:
            if reserva['hospede'] == hospede:
                for quarto in self.quartos:
                    if quarto['numero'] == reserva['quarto']:
                        return reserva['dias'] * quarto['diaria']
        return 0