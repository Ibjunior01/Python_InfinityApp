from operacoes import soma, subtracao, multiplicacao, divisao

while True:
    print("\n=== CALCULADORA ===")
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '5':
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opcao == '1':
        print("Resultado:", soma(a, b))
    elif opcao == '2':
        print("Resultado:", subtracao(a, b))
    elif opcao == '3':
        print("Resultado:", multiplicacao(a, b))
    elif opcao == '4':
        print("Resultado:", divisao(a, b))
    else:
        print("Opção inválida.")