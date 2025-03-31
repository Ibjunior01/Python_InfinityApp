"""
Para criar o ambiente virtual, use o seguinte comando:
python -m venv myenv ------ Substitua "myenv" pelo nome que você deseja dar ao seu ambiente virtual.

Para ativar: myenv/scripts/activate -- Após ativar verá o nome do ambiente no prompt. 

Agora que o ambiente virtual está ativo, você pode instalar bibliotecas e pacotes Python nele usando o pip.
    Exemplo: pip install nome_da_biblioteca

desativar o ambiente: deactivate.
"""
# Projeto com Funções 
"""
Definição de Dados
Cada tarefa será representada como um dicionário com as seguintes informações:
Nome: Nome da tarefa.
Descrição: Detalhes da tarefa.
Prioridade: Alta, Média ou Baixa.
Categoria: Trabalho, Pessoal, Estudos, etc.
Concluída: Status da tarefa (True ou False).
"""

#Adcionar tarefas
def adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

#Listar Tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for idx, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{idx}. {tarefa['nome']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status})")
        print(f"   Descrição: {tarefa['descricao']}")

#Marcar Tarefa como Concluída
def concluir_tarefa(tarefas, indice):
    if 0 < indice <= len(tarefas):
        tarefas[indice - 1]["concluida"] = True
        print(f"Tarefa '{tarefas[indice - 1]['nome']}' marcada como concluída!")
    else:
        print("Índice de tarefa inválido.")

#Filtrar Tarefas por Prioridade
def filtrar_por_prioridade(tarefas, prioridade):
    filtradas = [t for t in tarefas if t["prioridade"].lower() == prioridade.lower()]
    listar_tarefas(filtradas)

#Filtrar Tarefas por Categoria
def filtrar_por_categoria(tarefas, categoria):
    filtradas = [t for t in tarefas if t["categoria"].lower() == categoria.lower()]
    listar_tarefas(filtradas)

#Menu de Comandos -  loop para aceitar comandos até o usuário decidir sair.
def menu():
    tarefas = []

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (Alta/Média/Baixa): ")
            categoria = input("Categoria (Trabalho/Pessoal/Estudos): ")
            adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a marcar como concluída: "))
            concluir_tarefa(tarefas, indice)

        elif opcao == "4":
            prioridade = input("Digite a prioridade (Alta/Média/Baixa): ")
            filtrar_por_prioridade(tarefas, prioridade)

        elif opcao == "5":
            categoria = input("Digite a categoria (Trabalho/Pessoal/Estudos): ")
            filtrar_por_categoria(tarefas, categoria)

        elif opcao == "6":
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
