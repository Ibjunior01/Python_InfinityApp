import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print(" Adivinhe o número entre 1 e 100!")

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print(" Tente um número maior.")
    elif palpite > numero_secreto:
        print(" Tente um número menor.")
    else:
        print(f" Parabéns! Você acertou em {tentativas} tentativas.")
        break