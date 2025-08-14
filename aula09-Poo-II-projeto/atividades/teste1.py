from banco import ContaCorrente, ContaPoupanca

cc = ContaCorrente("001", "Ibermon", saldo=1000)
cc.depositar(500)
cc.sacar(1600)  # dentro do limite
cc.resumo()

cp = ContaPoupanca("002", "Ana", saldo=2000)
cp.adicionar_juros()
cp.resumo()
