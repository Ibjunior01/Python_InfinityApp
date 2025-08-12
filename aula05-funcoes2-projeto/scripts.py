from functools import reduce

# 01 - Média de três notas
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3
print("Média:", calcular_media(7.5, 8.0, 9.0))


# 02 - Área de retângulo
def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura
print("Área do retângulo:", calcular_area_retangulo(5, 3))


# 03 - Concatenar strings com *args
def concatenar_strings(*args):
    return ''.join(args)
print("Strings concatenadas:", concatenar_strings("Olá", " ", "Mundo", "!"))


# 04 - Dobro dos números com map
def dobrar_numeros(lista):
    return list(map(lambda x: x * 2, lista))
print("Dobro dos números:", dobrar_numeros([1, 2, 3, 4]))


# 05 - Filtrar números pares com filter
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))
print("Números pares:", filtrar_pares([1, 2, 3, 4, 5, 6]))


# 06 - Maior string com reduce
def maior_string(lista):
    return reduce(lambda a, b: a if len(a) > len(b) else b, lista)
print("Maior string:", maior_string(["banana", "abacaxi", "uva", "melancia"]))


# 07 - Lista de compras com *args
def criar_lista_de_compras(*args):
    return list(args)
print("Lista de compras:", criar_lista_de_compras("Arroz", "Feijão", "Macarrão"))


# 08 - Operações com lambda
def calcular_operacao(a, b, operacao):
    operacoes = {
        'soma': lambda x, y: x + y,
        'subtracao': lambda x, y: x - y,
        'multiplicacao': lambda x, y: x * y,
        'divisao': lambda x, y: x / y if y != 0 else 'Erro: divisão por zero'
    }
    return operacoes.get(operacao, lambda x, y: 'Operação inválida')(a, b)
print("Resultado da operação:", calcular_operacao(10, 5, "divisao"))


# 09 - Processador de texto com **kwargs
def processador_texto(texto, **kwargs):
    resultado = texto

    if kwargs.get('contar_palavras'):
        print(f"Total de palavras: {len(texto.split())}")

    if kwargs.get('contar_letras'):
        print(f"Total de letras: {len(texto.replace(' ', ''))}")

    if kwargs.get('inverter_texto'):
        resultado = resultado[::-1]

    if kwargs.get('substituir_palavra') and kwargs.get('nova_palavra'):
        resultado = resultado.replace(kwargs['substituir_palavra'], kwargs['nova_palavra'])

    return resultado

texto_original = "Python é poderoso e Python é divertido"
texto_processado = processador_texto(
    texto_original,
    contar_palavras=True,
    contar_letras=True,
    inverter_texto=False,
    substituir_palavra="Python",
    nova_palavra="JavaScript"
)
print("Texto processado:", texto_processado)
