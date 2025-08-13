class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.raca}, {self.idade} anos"



class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.peso}kg, {self.genero}"
    


class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} - R${self.salario:.2f}"

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome):
        self.funcionarios = [f for f in self.funcionarios if f.nome != nome]

    def listar_funcionarios(self):
        for f in self.funcionarios:
            print(f)




class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: divisão por zero"
        return a / b




class Fatura:
    def __init__(self, item, preco_unitario, quantidade):
        self.item = item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade
        return self.valor_total

    def __str__(self):
        return f"{self.item}: {self.quantidade} x R${self.preco_unitario:.2f} = R${self.valor_total:.2f}"
    



class FuncionarioHotel:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

class Quarto:
    def __init__(self, numero, diaria):
        self.numero = numero
        self.diaria = diaria
        self.status = "disponível"

class Reserva:
    def __init__(self, hospede, dias, quarto):
        self.hospede = hospede
        self.dias = dias
        self.quarto = quarto

class Hotel:
    def __init__(self):
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def adicionar_funcionario(self, nome, funcao, salario):
        self.funcionarios.append(FuncionarioHotel(nome, funcao, salario))

    def adicionar_quarto(self, numero, diaria):
        self.quartos.append(Quarto(numero, diaria))

    def fazer_reserva(self, hospede, dias, numero_quarto):
        for quarto in self.quartos:
            if quarto.numero == numero_quarto and quarto.status == "disponível":
                quarto.status = "ocupado"
                self.reservas.append(Reserva(hospede, dias, quarto))
                return f"Reserva feita para {hospede} no quarto {numero_quarto}"
        return "Quarto indisponível"

    def calcular_conta(self, hospede):
        for reserva in self.reservas:
            if reserva.hospede == hospede:
                return reserva.dias * reserva.quarto.diaria
        return 0
    
# Teste da classe Cachorro
dog = Cachorro("Bolt", "Labrador", 5)
print(dog)

# Teste da classe Pessoa
pessoa = Pessoa("Ana", 30, 65, "Feminino")
print(pessoa)

# Teste da Empresa
empresa = Empresa()
empresa.adicionar_funcionario(Funcionario("Carlos", "Analista", 4500))
empresa.adicionar_funcionario(Funcionario("Marina", "Gerente", 7000))
empresa.listar_funcionarios()

# Teste da Calculadora
calc = Calculadora()
print("Soma:", calc.somar(10, 5))
print("Divisão:", calc.dividir(10, 0))

# Teste da Fatura
fatura = Fatura("Notebook", 3500, 2)
fatura.gerar_fatura()
print(fatura)

# Teste do Hotel
hotel = Hotel()
hotel.adicionar_funcionario("João", "Recepcionista", 3000)
hotel.adicionar_quarto(101, 200)
hotel.adicionar_quarto(102, 250)
print(hotel.fazer_reserva("Maria", 3, 101))
print("Conta final:", hotel.calcular_conta("Maria"))