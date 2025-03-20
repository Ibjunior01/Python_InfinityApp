"""
IF, ELIF, ELSE: 

while:  O laço de repetição WHILE é usado para repetir uma sequência de instruções de maneira INDETERMINADA.
Este tipo de laço roda enquanto (while, em inglês) uma dada condição é True (verdadeira) e somente é interrompida quando a condição se torna False (falsa).

For: O for é um laço de repetição utilizado para percorrer ou iterar sobre uma sequência de dados, executando um conjunto de instruções em cada item de maneira DETERMINADA. 

Break: interrompe imediatamente a execução do loop, ignorando qualquer código restante dentro do loop.

Listas = [] - mutáveis
Tuplas = () - não mutáveis
Sets = { }

Dicionários: Dicionários são uma das estruturas de dados que permitem armazenar valores associados a chaves, formando assim uma espécie de “mapeamento” entre chaves e valores. Em outras palavras, um dicionário é uma coleção de pares chave-valor.

"""

#01 Peça a idade do usuário com base na idade fornecida, o programa deve classificar a pessoa em uma das seguintes ategorias: Se a idade for menor que 12 anos, imprimir "Criança". Se a idade estiver entre 12 e 17 anos (inclusive), imprimir "Adolescente". Se a idade estiver entre 18 e 59 anos (inclusive), imprimir "Adulto". Se a idade for igual ou superior a 60 anos, imprimir "Idoso". 

idade = int(input('Digite sua idade: '))
if idade < 12:
    print('Criança')
elif 12 <= idade <= 17:
    print('Adolescente')
elif 18 <= idade <= 59:
    print('Adulto')
else:
    print('Idoso')

# 02 Faça um programa que leia 3 números e informe o maior número e o menor. 

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

# 03 Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. 

pares = 0
impares = 0

for _ in range (10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1  # Incrementa o contador de pares
    else:
        impares += 1  # Incrementa o contador de ímpares

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")       

# 04 Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 

total_idades = 0
quantidade = 0

while True:
    idade = input("Digite a idade (ou 0 para encerrar): ")
    if idade == "0":
        break
    total_idades += int(idade)
    quantidade += 1

if quantidade > 0:
    media = total_idades / quantidade
    if 0 <= media <= 25:
        print("A turma é jovem.")
    elif 26 <= media <= 60:
        print("A turma é adulta.")
    else:
        print("A turma é idosa.")
else:
    print("Nenhuma idade foi inserida.")


# 05 Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. 

numeros = []

n = int(input("Quantos números você quer inserir? "))
for _ in range(n):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")


# Desafio: Gerenciamento de Compras de Produtos Você foi contratado para desenvolver um programa simples para auxiliar em um processo de compra de produtos. O programa deve permitir ao usuário inserir o nome e o preço de vários produtos, perguntando se deseja continuar inserindo mais produtos após cada entrada. Ao final, o programa deve fornecer um resumo da compra, incluindo: A) O total gasto na compra. B) A quantidade de produtos que custam mais de R$1000. C) O nome do produto mais barato. Desenvolva o programa em Python utilizando conceitos de entrada/saída de dados, condicionais e laços de repetição.

total_gasto = 0
produtos_mais_caros = 0
produto_mais_barato = ""
preco_mais_barato = float("inf")  # Inicializa com infinito

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    
    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_mais_caros += 1

    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    
    continuar = input("Deseja continuar inserindo produtos? (s/n): ").lower()
    if continuar != "s":
        break

print("\nResumo da compra:")
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_mais_caros}")
print(f"Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")
