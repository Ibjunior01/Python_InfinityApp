# calculadora simples

# Funções matemáticas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return None  # Retorna None para indicar erro
    return a / b

# Função principal da calculadora
def calculadora():
    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '5':
            print("Encerrando a calculadora. Até logo!")
            break

        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: você deve digitar números válidos.")
                continue

            if opcao == '1':
                resultado = soma(num1, num2)
                print(f"Resultado da soma: {resultado}")
            elif opcao == '2':
                resultado = subtracao(num1, num2)
                print(f"Resultado da subtração: {resultado}")
            elif opcao == '3':
                resultado = multiplicacao(num1, num2)
                print(f"Resultado da multiplicação: {resultado}")
            elif opcao == '4':
                resultado = divisao(num1, num2)
                if resultado is None:
                    print("Erro: divisão por zero não é permitida.")
                else:
                    print(f"Resultado da divisão: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()