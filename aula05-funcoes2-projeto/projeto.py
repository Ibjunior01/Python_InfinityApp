# gerenciador_tarefas.py

tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    tarefas.append(tarefa)

def listar_tarefas():
    for i, tarefa in enumerate(tarefas, 1):
        status = "ok" if tarefa['concluida'] else "erro "
        print(f"{i}. {tarefa['nome']} [{tarefa['prioridade']}] ({tarefa['categoria']}) - {status}")

def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True

def exibir_por_categoria(categoria):
    for tarefa in tarefas:
        if tarefa['categoria'].lower() == categoria.lower():
            print(f"- {tarefa['nome']} ({tarefa['prioridade']})")

def exibir_por_prioridade(prioridade):
    for tarefa in tarefas:
        if tarefa['prioridade'].lower() == prioridade.lower():
            print(f"- {tarefa['nome']} ({tarefa['categoria']})")

def menu():
    while True:
        print("\n MENU DE TAREFAS")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir por categoria")
        print("5. Exibir por prioridade")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (alta/média/baixa): ")
            categoria = input("Categoria: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)

        elif escolha == '2':
            listar_tarefas()

        elif escolha == '3':
            indice = int(input("Número da tarefa a marcar: ")) - 1
            marcar_concluida(indice)

        elif escolha == '4':
            cat = input("Categoria: ")
            exibir_por_categoria(cat)

        elif escolha == '5':
            pri = input("Prioridade: ")
            exibir_por_prioridade(pri)

        elif escolha == '6':
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

# Executar menu
if __name__ == "__main__":
    menu()