produtos = {}

for i in range(5):
    nome = input(f'Digite o nome do produto {i + 1}: ')
    preco = float(input(f'Digite o preço do produto {i + 1} (R$): '))
    produtos[nome] = preco # Armazena o nome como chave e o preço como valor

valor_total = sum(produtos.values())

print('\nProdutos e seus preços: ')
for nome, preco in produtos.items():
    print(f'{nome}: R${preco:.2f}')

print(f'\nO valor total da compra é: R${valor_total:.2f}')