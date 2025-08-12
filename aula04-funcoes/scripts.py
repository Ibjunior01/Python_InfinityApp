# 01 - Saudação personalizada
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")

# 02 - Saudação por horário
def saudacao_horario(horario):
    if 0 <= horario < 12:
        print("Bom dia!")
    elif 12 <= horario < 18:
        print("Boa tarde!")
    elif 18 <= horario <= 23:
        print("Boa noite!")
    else:
        print("Horário inválido.")

# 03 - Soma
def soma(a, b):
    return a + b

# 04 - Subtração
def subtracao(a, b):
    return a - b

# 05 - Multiplicação
def multiplicacao(a, b):
    return a * b

# 06 Calculadora com Rotinas e Unidade Lógica
# Funções de cálculo
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

# Funções de rotina
def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def executar_calculadora():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '5':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue

            if escolha == '1':
                print(f"Resultado: {soma(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicacao(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")


executar_calculadora()
