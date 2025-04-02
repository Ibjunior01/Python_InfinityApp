# Revisão Geral


#ATIVIDADE PRÁTICA 1 Dada uma lista de números, crie uma nova lista contendo apenas os números pares.
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(numeros)
print("Números pares:", pares)

#ATIVIDADE PRÁTICA 2 Crie um dicionário com informações de produtos, incluindo nome, preço e quantidade em estoque. Implemente funções para adicionar, remover e atualizar produtos no dicionário.
# Dicionário para armazenar produtos
estoque = {}

# Função para adicionar produtos
def adicionar_produto(nome, preco, quantidade):
    estoque[nome] = {"preco": preco, "quantidade": quantidade}
    print(f"Produto '{nome}' adicionado!")

# Função para remover produtos
def remover_produto(nome):
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido!")
    else:
        print("Produto não encontrado.")

# Função para atualizar quantidade
def atualizar_quantidade(nome, nova_quantidade):
    if nome in estoque:
        estoque[nome]["quantidade"] = nova_quantidade
        print(f"Quantidade de '{nome}' atualizada!")
    else:
        print("Produto não encontrado.")

# Teste das funções
adicionar_produto("Notebook", 2500, 5)
adicionar_produto("Mouse", 100, 20)
remover_produto("Mouse")
atualizar_quantidade("Notebook", 3)
print(estoque)

#ATIVIDADE PRÁTICA 3 Crie um conjunto com nomes de cores. Implemente uma função que retorne as cores que têm mais de quatro letras.
# Conjunto de cores
cores = {"azul", "vermelho", "verde", "amarelo", "roxo", "rosa"}

# Função para filtrar cores com mais de 4 letras
def cores_maiores_quatro_letras(conjunto_cores):
    return {cor for cor in conjunto_cores if len(cor) > 4}

# Exemplo de uso
resultado = cores_maiores_quatro_letras(cores)
print("Cores com mais de 4 letras:", resultado)

#ATIVIDADE PRÁTICA 4 Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings palíndromos.
# Função para identificar palíndromos
def filtrar_palindromos(lista):
    return [palavra for palavra in lista if palavra.lower() == palavra.lower()[::-1]]

# Exemplo de uso
palavras = ["ana", "carro", "radar", "python", "ovo"]
palindromos = filtrar_palindromos(palavras)
print("Palíndromos:", palindromos)

#ATIVIDADE PRÁTICA 5 Dado um dicionário que representa as vendas de produtos, encontre o produto mais vendido (ou os produtos mais vendidos, se houver um empate).
# Dicionário de vendas
vendas = {"Notebook": 15, "Celular": 30, "Mouse": 30, "Teclado": 10}

# Função para encontrar o produto mais vendido
def produto_mais_vendido(vendas):
    max_vendas = max(vendas.values())
    return [produto for produto, qtd in vendas.items() if qtd == max_vendas]

# Exemplo de uso
mais_vendidos = produto_mais_vendido(vendas)
print("Produto(s) mais vendido(s):", mais_vendidos)

#ATIVIDADE PRÁTICA 6 Receba uma lista de números e use funções agregadoras para contar quantos valores são ímpares e quantos são pares.
# Função para contar pares e ímpares
def contar_pares_impares(lista):
    pares = sum(1 for num in lista if num % 2 == 0)
    impares = sum(1 for num in lista if num % 2 != 0)
    return pares, impares

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = contar_pares_impares(numeros)
print(f"Pares: {pares}, Ímpares: {impares}")

#ATIVIDADE PRÁTICA 7 Você possui dados de vendas trimestrais de uma empresa em uma lista. Cada trimestre é representado como uma lista de números, onde cada número representa o valor de vendas de um mês (janeiro a março, abril a junho, julho a setembro e outubro a dezembro). Você deve realizar as seguintes tarefas: Calcule a média de vendas por trimestre.
#ATIVIDADE PRÁTICA Encontre o trimestre com a maior soma de vendas. Encontre o trimestre com a menor soma de vendas. Calcule o total de vendas no ano inteiro.
# Dados fictícios de vendas trimestrais
vendas_trimestrais = [
    [5000, 6000, 5500],  # Jan-Mar
    [7000, 8000, 7500],  # Abr-Jun
    [6500, 7200, 7800],  # Jul-Set
    [9000, 8500, 9200]   # Out-Dez
]

# Cálculo da média de vendas por trimestre
medias = [sum(trimestre) / len(trimestre) for trimestre in vendas_trimestrais]

# Encontra trimestre com maior e menor soma de vendas
trimestre_max = max(vendas_trimestrais, key=sum)
trimestre_min = min(vendas_trimestrais, key=sum)

# Calcula total anual de vendas
total_anual = sum(sum(trimestre) for trimestre in vendas_trimestrais)

print("Médias por trimestre:", medias)
print("Trimestre com maior vendas:", trimestre_max)
print("Trimestre com menor vendas:", trimestre_min)
print("Total anual de vendas:", total_anual)


#DESAFIO PRÁTICO Analise de Produção anual Você tem um conjunto de dados que contém informações sobre a produção anual de diferentes culturas em diversas fazendas ao longo de vários anos. O objetivo é realizar uma análise simples desses dados usando apenas as funções agregadoras.
#Tarefas: Encontre o ano em que a produção total foi máxima e o ano em que foi mínima. Identifique a cultura que teve a maior produção total e a cultura com a menor produção total ao longo dos anos. Encontre a fazenda que obteve a produção máxima em um determinado ano e a fazenda com a produção mínima no mesmo ano.
# Dados fictícios de produção agrícola
producao_anual = {
    2021: {"milho": 5000, "soja": 7000, "trigo": 3000},
    2022: {"milho": 5500, "soja": 7200, "trigo": 2800},
    2023: {"milho": 6000, "soja": 7500, "trigo": 3200},
}

# Encontra ano de maior e menor produção total
ano_max = max(producao_anual, key=lambda ano: sum(producao_anual[ano].values()))
ano_min = min(producao_anual, key=lambda ano: sum(producao_anual[ano].values()))

# Cultura de maior e menor produção
culturas = {cultura: sum(anos[cultura] for anos in producao_anual.values()) for cultura in producao_anual[2021]}
cultura_max = max(culturas, key=culturas.get)
cultura_min = min(culturas, key=culturas.get)

print(f"Ano com maior produção total: {ano_max}")
print(f"Ano com menor produção total: {ano_min}")
print(f"Cultura com maior produção: {cultura_max}")
print(f"Cultura com menor produção: {cultura_min}")
