from biblioteca import Livro, Membro, Biblioteca



livro1 = Livro("Desenvolvimento", "Guido", 101)
livro2 = Livro("javascript", "Ana", 102)
membro1 = Membro("Carlos", 1)

bib = Biblioteca()
bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)
bib.adicionar_membro(membro1)

bib.emprestar_livro(101, 1)
bib.pesquisar_livro("javascript")
bib.devolver_livro(101)
