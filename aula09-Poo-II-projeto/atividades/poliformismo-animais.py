class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

class Passaro(Animal):
    def emitir_som(self):
        print("Piu piu!")

animais = [Cachorro(), Gato(), Passaro()]
for animal in animais:
    animal.emitir_som()