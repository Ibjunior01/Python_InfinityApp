# Resumo aula passada
def quadrado(numero):
    resultado = numero ** 2
    return resultado

resultado = quadrado(5)
print('O quadrado de 5 é:', resultado)

#Atividade 01 Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas  usando uma função. A função deve receber as três notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada.
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Solicitar ao usuário que insira as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média chamando a função
media = calcular_media(nota1, nota2, nota3)

print(f"A média das notas é: {media:.2f}")

# *Args (Argumentos Posicionais Arbitrários) permite que você passe um número variável de argumentos posicionais para uma função. O operador *args permite que você chame a função com diferentes números de argumentos sem a necessidade de especificar quantos são. (TUPLAS)

# **Kwargs (Argumentos de Palavra Chave) permite que você passe um número indefinido de argumentos de palavra-chave para uma função. O operador ** antes de kwargs é usado para indicar que todos os argumentos de palavra-chave a seguir devem ser coletados no dicionário kwargs. (DICIONÁRIOS)

# Funções Lambda também conhecidas como funções anônimas, são funções pequenas e concisas que podem ser definidas em uma única linha de código. Elas são úteis quando você precisa de uma função simples que será usada apenas em um contexto específico.
quadrado = lambda x : x ** 2
print(f'o valor do quadrado de 5 é:', quadrado(5))

#ATIVIDADE PRÁTICA 3
#Crie uma função chamada concatenar_strings que aceita um número variável de strings como argumentos posicionais (usando *args). A função deve concatenar todas as strings em uma única string e retorná-la.
# Função para concatenar várias strings
def concatenar_strings(*args):
    return "".join(args)

# Exemplo de uso
resultado = concatenar_strings("Olá, ", "mundo", "!", " Python é incrível!")
print(resultado)

#ATIVIDADE PRÁTICA 4
#Crie uma função que aceita uma lista de números e use a função map para retornar uma nova lista contendo o dobro de cada número na lista de entrada.
# Função para dobrar os números de uma lista usando map
def dobrar_numeros(lista):
    return list(map(lambda x: x * 2, lista))

# Exemplo de uso
resultado = dobrar_numeros([1, 2, 3, 4])
print(resultado)

#ATIVIDADE PRÁTICA 5
#Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contendo apenas os números pares da lista de entrada.
# Função para filtrar números pares de uma lista usando filter
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

# Exemplo de uso
resultado = filtrar_pares([1, 2, 3, 4, 5, 6])
print(resultado)

#ATIVIDADE PRÁTICA 6
#Crie uma função que aceita uma lista de strings e use a função reduce (importada de functools) para encontrar a maior string na lista.
from functools import reduce

# Função para encontrar a maior string em uma lista usando reduce
def maior_string(lista):
    return reduce(lambda x, y: x if len(x) > len(y) else y, lista)

# Exemplo de uso
resultado = maior_string(["Python", "Incrível", "Simplesmente fantástico"])
print(resultado)

#ATIVIDADE PRÁTICA 7
#Crie uma função chamada criar_lista_de_compras que aceita um número variável de itens de compras como argumentos posicionais (usando *args). A função deve criar e retornar uma lista de compras que contenha todos os itens fornecidos.
# Função para criar uma lista de compras a partir de argumentos variáveis
def criar_lista_de_compras(*args):
    return list(args)

# Exemplo de uso
resultado = criar_lista_de_compras("Arroz", "Feijão", "Açúcar", "Café")
print(resultado)

#ATIVIDADE PRÁTICA 8
#Crie uma função que aceite dois números e uma operação (por exemplo, adição, subtração, multiplicação, divisão) como argumentos e use funções lambda para realizar a operação especificada. A função deve retornar o resultado da operação.
# Função para realizar operações matemáticas usando lambda
def calcular(num1, num2, operacao):
    operacoes = {
        "adição": lambda x, y: x + y,
        "subtração": lambda x, y: x - y,
        "multiplicação": lambda x, y: x * y,
        "divisão": lambda x, y: x / y if y != 0 else "Divisão por zero não é permitida."
    }
    return operacoes[operacao](num1, num2)

# Exemplo de uso
resultado = calcular(10, 2, "multiplicação")
print(resultado)

#DESAFIO PRÁTICO
    #Processador de Texto - passo 1
#Crie um processador de texto simples que realiza várias operações em um texto de entrada, como contar palavras, contar letras, inverter o texto e substituir palavras-chave. Requisitos: Crie uma função chamada processador_texto que aceite uma string de texto como argumento.
# Processador de texto simples
    #Processador de Texto - passo 2
#A função deve aceitar uma série de operações como argumentos de palavra-chave, usando **kwargs. As operações podem incluir "contar_palavras", "contar_letras", "inverter_texto" e "substituir_palavra".
#Use funções lambda para realizar as operações de acordo com as palavras-chave especificadas nos argumentos de palavra- chave.
def processador_texto(texto, **kwargs):
    resultado = texto
    
    if kwargs.get("contar_palavras"):
        print(f"Quantidade de palavras: {len(texto.split())}")
    
    if kwargs.get("contar_letras"):
        print(f"Quantidade de letras: {len(texto.replace(' ', ''))}")
    
    if kwargs.get("inverter_texto"):
        resultado = resultado[::-1]
        print(f"Texto invertido: {resultado}")
    
    if kwargs.get("substituir_palavra"):
        palavra_antiga = kwargs.get("substituir_palavra")
        nova_palavra = kwargs.get("nova_palavra")
        if palavra_antiga and nova_palavra:
            resultado = resultado.replace(palavra_antiga, nova_palavra)
            print(f"Texto após substituição: {resultado}")
    
    return resultado


#DESAFIO PRÁTICO
#Processador de Texto - passo 3
#Se a operação "substituir_palavra" for especificada, a função deve aceitar uma palavra-chave adicional, como "substituir_palavra" e "nova_palavra", para realizar a substituição em todo o texto.
#A função deve retornar o texto resultante após todas as operações.
# Processador de texto com múltiplas operações
def processador_texto(texto, **kwargs):
    resultado = texto  # Texto inicial

    # Contar palavras
    if kwargs.get("contar_palavras"):
        print(f"Quantidade de palavras: {len(texto.split())}")

    # Contar letras
    if kwargs.get("contar_letras"):
        print(f"Quantidade de letras: {len(texto.replace(' ', ''))}")

    # Inverter o texto
    if kwargs.get("inverter_texto"):
        resultado = resultado[::-1]
        print(f"Texto invertido: {resultado}")

    # Substituir palavra
    if kwargs.get("substituir_palavra") and kwargs.get("nova_palavra"):
        palavra_antiga = kwargs.get("substituir_palavra")
        nova_palavra = kwargs.get("nova_palavra")
        resultado = resultado.replace(palavra_antiga, nova_palavra)
        print(f"Texto após substituição: {resultado}")

    return resultado