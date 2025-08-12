print("=== Gerenciador de Compras ===")

total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ""
preco_mais_barato = None

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto (R$): "))

    total_gasto += preco

    if preco > 1000:
        produtos_acima_1000 += 1

    if preco_mais_barato is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

    continuar = input("Deseja adicionar mais produtos? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

print("\n=== Resumo da Compra ===")
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Produtos acima de R$1000: {produtos_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")