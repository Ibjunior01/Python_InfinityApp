import random

# Função para lançar dois dados e retornar a soma dos valores
def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma = dado1 + dado2

    return soma

resultado = lancar_dados()
print(f"Resultado do lançamento dos dados: {resultado}")
