"""
Sets: (conjunto) é uma coleção de elementos únicos e não ordenados. Uteis para operações matemáticas e tarefas que
envolvem coleções únicas de elementos.

Os Sets em Python nada mais são que Conjuntos Matemáticos. Neles, você também pode aplicar os conceitos de Interseção,
União, Diferença e etc.
"""

"""
#01 Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele: "maçã", "banana", "uva", "laranja" e"morango". Em seguida, imprima o conjunto.
frutas = set()

frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")

print("conjunto de frutas: ", frutas)

#02 Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.
if 'banana' in frutas:
    print('Banana está presente.')
else:
    print('Banana não está presente.')

#03 Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele: "morango", "cereja" e "framboesa". Em seguida, imprima o conjunto.
frutas_vermelhas = set()

frutas_vermelhas.add("morango")
frutas_vermelhas.add("cereja")
frutas_vermelhas.add("framboesa")

# Impressão do conjunto
print("Conjunto de frutas vermelhas:", frutas_vermelhas)

#04 Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.
frutas_vermelhas.remove("cereja")
print("Conjunto atualizado de frutas vermelhas:", frutas_vermelhas)

#05 Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

uniao = a.union(b)
print('A união dos conjuntos a e b é:', uniao)

#06 Crie um programa que recebe dois conjuntos e exibe a interseção deles.
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

intersecao = conjunto1.intersection(conjunto2)

print("A interseção dos dois conjuntos é:", intersecao)

#07 Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.
lista1 = [1, 2, 2, 3, 4]
lista2 = [3, 4, 4, 5, 6]

# Conversão das listas em conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# União dos elementos únicos
uniao_listas = conjunto1.union(conjunto2)

# Exibição do resultado
print("A união dos elementos únicos das listas é:", uniao_listas)
"
"""

"""
Dicionários são uma das estruturas de dados que permitem armazenar valores associados a chaves {}, formando assim uma espécie e “mapeamento” entre chaves e valores. Em outras palavras, um dicionário é uma coleção de pares chave-valor(:).

"""
#08 Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.
pessoas = {
    "Pessoa1": {"nome": "Ana", "idade": 25},
    "Pessoa2": {"nome": "Carlos", "idade": 30},
    "Pessoa3": {"nome": "Bianca", "idade": 22}
}
print("Informações de pessoas:")
for chave, valor in pessoas.items():
    print(f"{chave}: Nome = {valor['nome']}, Idade = {valor['idade']}")


#09 Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.
# Criação de um dicionário simples
dicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3"
}

# Percorrer e exibir apenas as chaves
print("Chaves do dicionário:")
for chave in dicionario.keys():
    print(chave)

# Percorrer e exibir apenas os valores
print("\nValores do dicionário:")
for valor in dicionario.values():
    print(valor)

#10 Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existir.
# Função para adicionar ou atualizar uma chave no dicionário
def adicionar_ou_atualizar(dicionario, chave, valor):
    dicionario[chave] = valor  # Adiciona ou atualiza a chave com o valor
    return dicionario

# Exemplo de uso
meu_dicionario = {"nome": "Ana", "idade": 25}
meu_dicionario = adicionar_ou_atualizar(meu_dicionario, "idade", 30)  # Atualiza
meu_dicionario = adicionar_ou_atualizar(meu_dicionario, "cidade", "Fortaleza")  # Adiciona
print(meu_dicionario)

#11 Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso contrário.
# Função para verificar se todas as chaves estão no dicionário
def verificar_chaves(dicionario, lista_chaves):
    return all(chave in dicionario for chave in lista_chaves)  # Retorna True se todas existirem

# Exemplo de uso
meu_dicionario = {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"}
chaves_para_verificar = ["nome", "idade"]
resultado = verificar_chaves(meu_dicionario, chaves_para_verificar)
print(resultado)  # True


#12 Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.
# Função para sistema de votação
def sistema_de_votacao():
    votos = {}
    while True:
        print("\nDigite 0 para encerrar a votação.")
        voto = input("Escolha sua opção de voto: ")
        
        if voto == "0":
            break  # Encerra a votação
        
        if voto in votos:
            votos[voto] += 1  # Incrementa o voto
        else:
            votos[voto] = 1  # Adiciona nova opção com um voto
    
    print("\nResultado Final da Votação:")
    for opcao, num_votos in votos.items():
        print(f"{opcao}: {num_votos} votos")

# Exemplo de uso
sistema_de_votacao()


#13 Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.
# Dicionário de alunos e suas notas
alunos = {
    "Ana": [8.5, 7.0, 9.0],
    "Carlos": [6.5, 7.5, 8.0],
    "Bianca": [9.0, 8.5, 7.5]
}

# Cálculo da média de cada aluno
for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno}: Média = {media:.2f}")


#14 Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas. 
# Função para remover duplicatas
def remover_duplicatas(lista):
    return list(set(lista))

# Exemplo de uso
numeros = [1, 2, 2, 3, 4, 4, 5]
numeros_sem_duplicatas = remover_duplicatas(numeros)
print("Lista original:", numeros)
print("Lista sem duplicatas:", numeros_sem_duplicatas)


# 15 Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante. 
# Função para unir múltiplos conjuntos
def uniao_conjuntos(*conjuntos):
    return set().union(*conjuntos)

# Exemplo de uso
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5}
conjunto3 = {3, 6}
resultado = uniao_conjuntos(conjunto1, conjunto2, conjunto3)
print("União dos conjuntos:", resultado)


#DESAFIO PRÁTICO 1 Sistema de Cadastro de Alunos - passo 1 Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas: Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: ' nome ' , 'idade ' , ' notas '. As notas devem ser armazenadas em uma tupla. 
 # Sistema de Cadastro de Alunos
alunos = []

while True:
    print("\nDigite 0 para encerrar.")
    nome = input("Nome do aluno: ")
    if nome == "0":
        break
    idade = int(input("Idade do aluno: "))
    notas = (
        float(input("Nota em Matemática: ")),
        float(input("Nota em Ciências: ")),
        float(input("Nota em História: "))
    )
    aluno = {"nome": nome, "idade": idade, "notas": notas}
    alunos.append(aluno)

print("\nAlunos cadastrados:", alunos)


# DESAFIO PRÁTICO 2 Sistema de Cadastro de Alunos - passo 2 Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas informações de forma organizada. Média de Notas: O programa deve calcular a média das notas de cada aluno e exibi-la. Aluno com Melhor Média: O programa deve identificar e exibir o aluno com a melhor média de notas.
# Visualizar alunos e calcular médias
def exibir_alunos(alunos):
    print("\nInformações dos alunos:")
    for aluno in alunos:
        media = sum(aluno["notas"]) / len(aluno["notas"])
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Média: {media:.2f}")

def calcular_melhor_media(alunos):
    melhor_aluno = max(alunos, key=lambda a: sum(a["notas"]) / len(a["notas"]))
    melhor_media = sum(melhor_aluno["notas"]) / len(melhor_aluno["notas"])
    print(f"\nAluno com Melhor Média: {melhor_aluno['nome']}, Média: {melhor_media:.2f}")

# Exemplo com alunos cadastrados
exibir_alunos(alunos)
calcular_melhor_media(alunos)
