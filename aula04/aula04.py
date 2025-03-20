"""
Função: Uma função é como uma mini-fábrica que realiza uma tarefa específica. 

def saudacao ( nome ): ## saudacao = nome da função e nome = parâmetro
    print('olá')
sadacacao( ) # Exibe olá no terminal

O return é usado para especificar o que a função deve retornar, sempre que usar o return e quiser exibir o resultado obtido, terá que ser usado o print()

O paradigma funcional: é um estilo de programação onde a base são as funções. Ele foca em realizar computações através da avaliação de funções, evitando mudança de estado e dados mutáveis.

Documentar suas funções é essencial para que outros desenvolvedores (ou você mesmo no futuro) possam entender o que a unção faz, quais parâmetros ela recebe e o que ela retorna.


"""

#01 Crie uma função que receba um nome e imprima uma saudação personalizada. 
def saudacao (nome):
    print(f'Olá, {nome}! Seja bem-vindo(a).')

saudacao('Júnior')

#02 Crie uma função que receba um horário e imprima "Bom dia!" , "Boa tarde!" ou "Boa noite!" conforme o horário. 

def saudacao_horario (horario):
    if 0 <= horario < 12:
        print("Bom dia!")
    elif 12 <= horario < 18:
        print("Boa tarde!")
    elif 18 <= horario < 24:
        print("Boa noite!")
    else:
        print("Horário inválido!")

saudacao_horario(15)

#03 Crie uma função que receba dois números e retorne a soma deles. 

def somar (num1, num2):
    return num1 + num2

resultado = somar(5, 7)
print(f'A soma é: {resultado}')

#04 Crie uma função que receba dois números e retorne a subtração do primeiro pelo segundo. 

def subtrair(num1, num2):
    return num1 - num2

# Exemplo de uso
resultado = subtrair(10, 4)
print(f"A subtração é: {resultado}")

#05 Crie uma função que receba dois números e retorne a multiplicação deles. 

def multiplicar(num1, num2):
    return num1 * num2

# Exemplo de uso
resultado = multiplicar(3, 5)
print(f"A multiplicação é: {resultado}")

#DESAFIO: Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair. (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.) Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos. Dica: Utilize de condicionais e Laços de Repetição para realizar esse exercício.

# Funções de operações
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."

# Função principal da calculadora
def calculadora():
    while True:
        print("\nCalculadora:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Saindo da calculadora. Até logo!")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {soma(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado: {subtracao(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif opcao == "4":
            print(f"Resultado: {divisao(num1, num2)}")
        else:
            print("Opção inválida! Tente novamente.")

# Exemplo de uso
calculadora()

