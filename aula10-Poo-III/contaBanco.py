class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial
        self._transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._transacoes.append(f"Depósito: R${valor:.2f}")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            self._transacoes.append(f"Saque: R${valor:.2f}")
        else:
            print("Operação inválida.")

    def exibir_saldo(self):
        print(f"Saldo de {self._titular}: R${self._saldo:.2f}")

    def historico(self):
        print("Transações:")
        for t in self._transacoes:
            print(f"- {t}")

# Exemplo de uso
conta = ContaBancaria("Ibermon", 100)
conta.depositar(50)
conta.sacar(30)
conta.exibir_saldo()
conta.historico()