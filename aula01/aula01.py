"""
Lista = []: Uma lista em Python é uma estrutura de dados que pode conter vários elementos em uma sequência ordenada. Para criar a lista com os números de 1 a 5, você simplesmente insere esses números dentro dos colchetes, separados por vírgulas.

Se quisermos exibir apenas um dos valores guardados na lista, basta especificarmos a
posição (índice) da lista onde o valor desejado se encontra. Começa com 0, 1, 2 ...
"""


#01 Faça a definição de uma lista contendo os números de 1 até 5. Finalmente, utilize o print() para exibir os valores da lista.
numeros = [1, 2, 3, 4, 5]
print (f'Os valores da lista são: {numeros}')

#02 Faça a definição de uma lista contendo as vogais.Finalmente, utilize o print() para exibir os valores da lista.
vogais = ['a', 'e', 'i', 'o', 'u']
print (f'As vogais são: {vogais}')

#03 Defina uma lista com 5 itens que tenha, pelo menos, 3 classes diferentes. Utilize o print() para exibir o terceiro elemento dessa lista.
lista = ['Casa', 1, 'a', 3.14]
print(lista[3])

"""
Manupulação de listas
Adição .append() Adicionar um elemento ao final da lista
adição .insert() Adicionar um elemento na posição informada
Remoção .remove() Remover um elemento de uma lista através de seu valor
remoção .pop() Remover um elemento de uma lista através de seu índice
"""

"""
Tuplas = (): são estruturas semelhantes a listas, mas com uma distinção importante: são imutáveis, serve para garantir a integridade dos dados.
"""

#04 Crie uma tupla para representar as informações de três palestrantes, cada uma contendo o nome, o tema da palestra e a instituição à qual estão vinculados. Exiba na tela as informações do terceiro palestrante, incluindo nome, tema da palestra e instituição.

palestrantes = (
    ("João Silva", "Inovação Tecnológica", "Universidade de São Paulo"),
    ("Maria Oliveira", "Sustentabilidade no Século XXI", "Universidade Federal do Ceará"),
    ("Carlos Souza", "Inteligência Artificial e o Futuro", "Instituto Tecnológico de Aeronáutica")
)

# Exibição das informações do terceiro palestrante
terceiro_palestrante = palestrantes[2]
print("Informações do terceiro palestrante:")
print("Nome:", terceiro_palestrante[0])
print("Tema da Palestra:", terceiro_palestrante[1])
print("Instituição:", terceiro_palestrante[2])

#Desafio prático
# Lista de tuplas representando as equipes e suas pontuações
resultados = [
    ("Equipe A", [8, 9, 7, 6]),
    ("Equipe B", [10, 8, 9, 10]),
    ("Equipe C", [5, 7, 6, 8])
]

# 1. Calcule a média das pontuações de cada equipe
medias = [(equipe, sum(pontos) / len(pontos)) for equipe, pontos in resultados]

# 2. Ordene a lista medias em ordem decrescente de pontuação média
medias.sort(key=lambda x: x[1], reverse=True)

# 3. Crie uma lista chamada classificacao (já ordenada)
classificacao = medias

# 4. Exiba a classificação final das equipes
print("Classificação Final:")
for equipe, media in classificacao:
    print(f"{equipe}: Média = {media:.2f}")

