"""
Módulos: divisão do código em diferentes ariquivos .py (importar com a intrução: import)
"""

#ATIVIDADE PRÁTICA 1 Crie um programa que será uma calculadora. Nesta calculadora você deverá ter um módulo para as operações atemáticas,  o arquivo principal deverá conter apenas um menu de escolha para o suário (soma, subtração, multiplicação e divisão).
import operacoes # importa o módulo criado.

def menu():
    while True: # para rodar continuamente até o usuário escolher sair ().
        print("\nCalculadora:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Encerrando a calculadora. Até logo!")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {operacoes.soma(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado: {operacoes.subtracao(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado: {operacoes.multiplicacao(num1, num2)}")
        elif opcao == "4":
            print(f"Resultado: {operacoes.divisao(num1, num2)}")
        else:
            print("Opção inválida, tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()


#ATIVIDADE PRÁTICA 2 Crie um módulo chamado manipulacao_strings que contenha funções para realizar operações com strings, como inverter uma string, contar o número de palavras em uma string e verificar se uma string é um palíndromo (lê-se igual de trás para frente). Crie um programa principal que importe o módulo e use essas funções com strings fornecidas pelo usuário.
#Este arquivo importará o módulo  e terá um menu interativo.
import manipulacao_strings

# Menu para interagir com o usuário
def menu_strings():
    while True:
        print("\nManipulação de Strings:")
        print("1. Inverter String")
        print("2. Contar Palavras")
        print("3. Verificar se é Palíndromo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "4":
            print("Encerrando o programa. Até logo!")
            break

        texto = input("Digite um texto: ")

        if opcao == "1":
            print(f"Texto invertido: {manipulacao_strings.inverter_string(texto)}")
        elif opcao == "2":
            print(f"Quantidade de palavras: {manipulacao_strings.contar_palavras(texto)}")
        elif opcao == "3":
            if manipulacao_strings.eh_palindromo(texto):
                print("É um palíndromo!")
            else:
                print("Não é um palíndromo.")
        else:
            print("Opção inválida, tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu_strings()

"""
Bibliotecas: para utilizar funcionalidades prontas e desenvolver de forma mais eficiente. 
import math : conjunto de funções matemáticas e constantes para realizar cálculos matemáticos.
import random : é usada para gerar números aleatórios, embaralhar listas, escolher elementos aleatórios e muito mais.

"""
#ATIVIDADE PRÁTICA 3 Crie um programa que permite ao usuário calcular a área e operímetro de formas geométricas simples, como quadrados, retângulos e círculos. Use funções matemáticas do módulo math para realizar os cálculos.
import math

# Função para calcular área e perímetro de um quadrado
def quadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

# Função para calcular área e perímetro de um retângulo
def retangulo(largura, altura):
    area = largura * altura
    perimetro = 2 * (largura + altura)
    return area, perimetro

# Função para calcular área e perímetro de um círculo
def circulo(raio):
    area = math.pi * (raio ** 2)
    perimetro = 2 * math.pi * raio
    return area, perimetro

# Menu de opções
def menu():
    print("Escolha uma forma geométrica:")
    print("1. Quadrado")
    print("2. Retângulo")
    print("3. Círculo")
    escolha = input("Digite a opção: ")

    if escolha == "1":
        lado = float(input("Digite o lado do quadrado: "))
        area, perimetro = quadrado(lado)
    elif escolha == "2":
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area, perimetro = retangulo(largura, altura)
    elif escolha == "3":
        raio = float(input("Digite o raio do círculo: "))
        area, perimetro = circulo(raio)
    else:
        print("Opção inválida.")
        return

    print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

# Executa o programa
menu()

# ATIVIDADE PRÁTICA 4 Desenvolva um jogo de adivinhação em que o programa escolhe um número aleatório e desafia o jogador a adivinhá-lo. Forneça dicas ao jogador, indicando se o número é maior ou menor do que a adivinhação atual.
import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)  # Número aleatório entre 1 e 100
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação! Tente adivinhar o número entre 1 e 100.")

    while True:
        tentativa = int(input("Digite seu palpite: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior!")
        elif tentativa > numero_secreto:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

# Executa o jogo
jogo_adivinhacao()

# ATIVIDADE PRÁTICA 5 Desenvolva um programa que permita ao usuário converter entre diferentes unidades de medida, como metros para pés, quilogramas para libras, ou Celsius para Fahrenheit. Use módulos que contenham funções de conversão.
import conversor

def menu_conversao():
    print("Escolha uma conversão:")
    print("1. Metros para Pés")
    print("2. Quilogramas para Libras")
    print("3. Celsius para Fahrenheit")
    escolha = input("Digite a opção: ")

    if escolha == "1":
        metros = float(input("Digite a quantidade de metros: "))
        print(f"{metros} metros = {conversor.metros_para_pes(metros):.2f} pés")
    elif escolha == "2":
        kg = float(input("Digite a quantidade de quilogramas: "))
        print(f"{kg} kg = {conversor.kg_para_libras(kg):.2f} libras")
    elif escolha == "3":
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C = {conversor.celsius_para_fahrenheit(celsius):.2f}°F")
    else:
        print("Opção inválida.")

menu_conversao()

# DESAFIO PRÁTICO Gerenciador de Livros de Biblioteca - passo 1
#Crie um programa que permita aos usuários: Adicionar novos livros à biblioteca, com informações como título, autor e número de cópias disponíveis. Listar todos os livros disponíveis na biblioteca. Permitir aos usuários fazer empréstimos de livros, reduzindo o número de cópias disponíveis quando um livro é emprestado.


# DESAFIO PRÁTICO Gerenciador de Livros de Biblioteca - passo 2
#Permitir aos usuários devolver livros, aumentando o número de cópias disponíveis quando um livro é devolvido. Verificar a disponibilidade de um livro específico na biblioteca. Mostrar a lista de livros emprestados a um usuário específico.
