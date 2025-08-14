class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.emprestado = False

class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def emprestar_livro(self, id_livro, numero_membro):
        livro = next((l for l in self.catalogo if l.id == id_livro and not l.emprestado), None)
        membro = next((m for m in self.membros if m.numero_membro == numero_membro), None)
        if livro and membro:
            livro.emprestado = True
            membro.historico.append(livro)
            print(f"Livro '{livro.titulo}' emprestado para {membro.nome}")
        else:
            print("Livro indisponível ou membro não encontrado")

    def devolver_livro(self, id_livro):
        livro = next((l for l in self.catalogo if l.id == id_livro), None)
        if livro:
            livro.emprestado = False
            print(f"Livro '{livro.titulo}' devolvido")

    def pesquisar_livro(self, termo):
        resultados = [l for l in self.catalogo if termo.lower() in l.titulo.lower() or termo.lower() in l.autor.lower() or termo == str(l.id)]
        for l in resultados:
            status = "Emprestado" if l.emprestado else "Disponível"
            print(f"{l.id} - {l.titulo} ({l.autor}) - {status}")