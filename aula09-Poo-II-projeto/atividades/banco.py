class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")

    def resumo(self):
        print(f"Conta: {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, taxa=10, limite=500):
        super().__init__(numero, titular, saldo)
        self.taxa = taxa
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Limite excedido")

    def resumo(self):
        print(f"[Conta Corrente] {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, juros=0.02):
        super().__init__(numero, titular, saldo)
        self.juros = juros

    def adicionar_juros(self):
        self.saldo += self.saldo * self.juros

    def resumo(self):
        print(f"[Conta Poupança] {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}")