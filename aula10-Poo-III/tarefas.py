class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        print(f"Tarefas do projeto '{self.nome}':")
        for tarefa in self.tarefas:
            print(f"- {tarefa.descricao}")

# Exemplo de uso
projeto = Projeto("Site Pessoal")
projeto.adicionar_tarefa(Tarefa("Criar layout"))
projeto.adicionar_tarefa(Tarefa("Implementar backend"))
projeto.listar_tarefas()