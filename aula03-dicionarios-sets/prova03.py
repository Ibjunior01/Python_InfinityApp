print("=== Sistema de Cadastro de Alunos ===")

alunos = []

while True:
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    
    print("Digite as notas do aluno:")
    matematica = float(input("Matemática: "))
    ciencias = float(input("Ciências: "))
    historia = float(input("História: "))
    
    notas = (matematica, ciencias, historia)
    
    aluno = {
        'nome': nome,
        'idade': idade,
        'notas': notas
    }
    
    alunos.append(aluno)
    
    continuar = input("Deseja cadastrar outro aluno? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

print("\n=== Lista de Alunos Cadastrados ===")

melhor_media = -1
melhor_aluno = None

for aluno in alunos:
    nome = aluno['nome']
    idade = aluno['idade']
    notas = aluno['notas']
    media = sum(notas) / len(notas)
    
    print(f"\nNome: {nome}")
    print(f"Idade: {idade}")
    print(f"Notas: Matemática={notas[0]}, Ciências={notas[1]}, História={notas[2]}")
    print(f"Média: {media:.2f}")
    
    if media > melhor_media:
        melhor_media = media
        melhor_aluno = aluno

print("\n=== Aluno com a Melhor Média ===")
print(f"Nome: {melhor_aluno['nome']}")
print(f"Média: {melhor_media:.2f}")