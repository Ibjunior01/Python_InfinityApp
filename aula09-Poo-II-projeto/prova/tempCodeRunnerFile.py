from biblioteca import Livro, Membro, Biblioteca
from banco import ContaCorrente, ContaPoupanca


livro1 = Livro("Python para Iniciantes", "Guido", 101)
livro2 = Livro("POO com Python", "Ana", 102)
membro1 = Membro("Carlos", 1)

bib = Biblioteca()
bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)
bib.adicionar_membro(membro1)

bib.emprestar_livro(101, 1)
bib.pesquisar_livro("Python")
bib.devolver_livro(101)
