# DESAFIO PRÁTICO: Gerenciador de Livros - Passo 1

biblioteca = {}  # Dicionário para armazenar os livros

def adicionar_livro(titulo, autor, copias):
    biblioteca[titulo] = {"autor": autor, "copias": copias}
    print(f"Livro '{titulo}' adicionado com sucesso!")

def listar_livros():
    if not biblioteca:
        print("Nenhum livro disponível.")
        return
    for titulo, info in biblioteca.items():
        print(f"'{titulo}' por {info['autor']} - Cópias disponíveis: {info['copias']}")

def emprestar_livro(titulo):
    if titulo in biblioteca and biblioteca[titulo]["copias"] > 0:
        biblioteca[titulo]["copias"] -= 1
        print(f"Você emprestou '{titulo}'.")
    else:
        print("Livro indisponível.")

# Testando as funções
adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 3)
adicionar_livro("Dom Casmurro", "Machado de Assis", 2)
listar_livros()
emprestar_livro("Dom Casmurro")
listar_livros()

# DESAFIO PRÁTICO: Gerenciador de Livros - Passo 2
def devolver_livro(titulo):
    if titulo in biblioteca:
        biblioteca[titulo]["copias"] += 1
        print(f"Livro '{titulo}' devolvido com sucesso.")
    else:
        print("Este livro não pertence à biblioteca.")

def verificar_disponibilidade(titulo):
    if titulo in biblioteca:
        return biblioteca[titulo]["copias"] > 0
    return False

def livros_emprestados(usuario):
    print(f"Livros emprestados por {usuario}:")
    for titulo, info in biblioteca.items():
        if info["copias"] == 0:
            print(f"- {titulo}")

# Testando novas funções
devolver_livro("Dom Casmurro")
listar_livros()
print("Disponibilidade de 'Dom Casmurro':", verificar_disponibilidade("Dom Casmurro"))