from manipulacao_strings import inverter, contar_palavras, eh_palindromo

texto = input("Digite uma frase: ")

print("Invertida:", inverter(texto))
print("Número de palavras:", contar_palavras(texto))
print("É palíndromo?", "Sim" if eh_palindromo(texto) else "Não")