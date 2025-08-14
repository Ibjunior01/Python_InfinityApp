class Aluno:
    def __init__(self, nome, idade, matricula):
        self._nome = nome
        self._idade = idade
        self._matricula = matricula

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        self._idade = nova_idade

    def get_matricula(self):
        return self._matricula

# Exemplo de uso
aluno = Aluno("Ana", 20, "2025A001")
print(aluno.get_nome())
aluno.set_nome("Ana Clara")
print(aluno.get_nome())