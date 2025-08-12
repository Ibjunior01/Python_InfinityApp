from conversor import metros_para_pes, kg_para_libras, celsius_para_fahrenheit

print("1 - Metros para pés\n2 - Kg para libras\n3 - Celsius para Fahrenheit")
opcao = input("Escolha: ")

valor = float(input("Digite o valor: "))

if opcao == '1':
    print("Resultado:", metros_para_pes(valor))
elif opcao == '2':
    print("Resultado:", kg_para_libras(valor))
elif opcao == '3':
    print("Resultado:", celsius_para_fahrenheit(valor))
else:
    print("Opção inválida.")