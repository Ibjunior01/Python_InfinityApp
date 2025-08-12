from sistema import *

while True:
    print("\n MENU BIBLIOTECA")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Verificar disponibilidade")
    print("6 - Ver livros emprestados")
    print("7 - Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        t = input("Título: ")
        a = input("Autor: ")
        c = int(input("Cópias: "))
        adicionar_livro(t, a, c)

    elif opcao == '2':
        listar_livros()

    elif opcao == '3':
        u = input("Usuário: ")
        t = input("Título do livro: ")
        emprestar_livro(u, t)

    elif opcao == '4':
        u = input("Usuário: ")
        t = input("Título do livro: ")
        devolver_livro(u, t)

    elif opcao == '5':
        t = input("Título do livro: ")
        verificar_disponibilidade(t)

    elif opcao == '6':
        u = input("Usuário: ")
        livros_emprestados(u)

    elif opcao == '7':
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")