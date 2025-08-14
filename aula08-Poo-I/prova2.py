# Classe Animal
class Animal:
    def falar(self):
        print("Este animal faz um som genérico.")

# Classe Cachorro
class Cachorro:
    def falar(self):
        print("O cachorro está latindo.")

# Classe Gato
class Gato:
    def falar(self):
        print("O gato está miando.")

# Criando objetos e chamando o método falar()
animal = Animal()
cachorro = Cachorro()
gato = Gato()

animal.falar()
cachorro.falar()
gato.falar()