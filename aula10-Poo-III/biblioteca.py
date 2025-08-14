class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

class Usuario:
    def __init__(self, nome, id_usuario):
        self._nome = nome
        self._id = id_usuario

    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id

class Biblioteca:
    def __init__(self):
        self._livros = []

    def adicionar_livro(self, livro):
        self._livros.append(livro)

    def remover_livro(self, livro):
        if livro in self._livros:
            self._livros.remove(livro)

    def listar_livros(self):
        print("Livros disponíveis:")
        for livro in self._livros:
            print(f"- {livro.get_titulo()} ({livro.get_autor()})")

    def verificar_disponibilidade(self, livro):
        return livro in self._livros

class Emprestimo:
    def __init__(self, usuario, livro, biblioteca):
        if biblioteca.verificar_disponibilidade(livro):
            self._usuario = usuario
            self._livro = livro
            biblioteca.remover_livro(livro)
            print(f"{usuario.get_nome()} emprestou '{livro.get_titulo()}'.")
        else:
            print(f"O livro '{livro.get_titulo()}' não está disponível.")

# Exemplo de uso
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")
usuario = Usuario("Ibermon", "U001")
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()
emprestimo = Emprestimo(usuario, livro1, biblioteca)
biblioteca.listar_livros()