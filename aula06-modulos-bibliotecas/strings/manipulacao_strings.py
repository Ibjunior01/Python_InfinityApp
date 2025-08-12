def inverter(texto):
    return texto[::-1]

def contar_palavras(texto):
    return len(texto.split())

def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]