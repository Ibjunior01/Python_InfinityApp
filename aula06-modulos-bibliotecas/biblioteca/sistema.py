livros = []
emprestimos = {}

def adicionar_livro(titulo, autor, copias):
    livros.append({'titulo': titulo, 'autor': autor, 'copias': copias})

def listar_livros():
    for livro in livros:
        print(f"{livro['titulo']} - {livro['autor']} ({livro['copias']} disponíveis)")

def emprestar_livro(usuario, titulo):
    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            if livro['copias'] > 0:
                livro['copias'] -= 1
                emprestimos.setdefault(usuario, []).append(titulo)
                print("Livro emprestado com sucesso.")
                return
            else:
                print("Livro indisponível.")
                return
    print("Livro não encontrado.")

def devolver_livro(usuario, titulo):
    if usuario in emprestimos and titulo in emprestimos[usuario]:
        emprestimos[usuario].remove(titulo)
        for livro in livros:
            if livro['titulo'].lower() == titulo.lower():
                livro['copias'] += 1
                print("Livro devolvido com sucesso.")
                return
    else:
        print("Esse livro não está emprestado para este usuário.")

def verificar_disponibilidade(titulo):
    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            print(f"{livro['copias']} cópias disponíveis.")
            return
    print("Livro não encontrado.")

def livros_emprestados(usuario):
    print(f"Livros emprestados para {usuario}:")
    for livro in emprestimos.get(usuario, []):
        print(f"- {livro}")