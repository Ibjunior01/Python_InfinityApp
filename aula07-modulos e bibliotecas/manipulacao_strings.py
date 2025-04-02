#Atividade 02
# Função para inverter uma string
def inverter_string(texto):
    return texto[::-1] # para inverter a string.

# Função para contar o número de palavras em uma string
def contar_palavras(texto):
    return len(texto.split())

# Função para verificar se uma string é um palíndromo
def eh_palindromo(texto):
    texto_limpo = texto.lower().replace(" ", "")  # Remove espaços e padroniza minúsculas
    return texto_limpo == texto_limpo[::-1]  # Compara a string original com ela invertida