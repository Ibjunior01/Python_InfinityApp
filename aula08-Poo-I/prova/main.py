from listas_e_tuplas import filtrar_pares
from produtos import adicionar_produto, remover_produto, atualizar_produto, produtos
from cores import cores_maiores_que_quatro
from strings import strings_palindromos
from agregadoras import produto_mais_vendido, contar_pares_impares, media_por_trimestre
from producao_agricola import dados, producao_total_por_ano, cultura_maior_menor, fazenda_extremos_por_ano
from hotel import Hotel

# Testes rápidos
print("Números pares:", filtrar_pares([1, 2, 3, 4, 5, 6]))

adicionar_produto("Arroz", 5.5, 20)
atualizar_produto("Arroz", estoque=15)
print("Produtos:", produtos)

print("Cores com mais de 4 letras:", cores_maiores_que_quatro({"azul", "vermelho", "rosa", "amarelo"}))

print("Palíndromos:", strings_palindromos(["ana", "casa", "radar", "python"]))

vendas = {"Arroz": 50, "Feijão": 50, "Macarrão": 30}
print("Mais vendidos:", produto_mais_vendido(vendas))

pares, impares = contar_pares_impares([1, 2, 3, 4, 5])
print(f"Pares: {pares}, Ímpares: {impares}")

trimestres = [[1000, 1200, 1100], [1300, 1250, 1400], [1500, 1600, 1550], [1700, 1650, 1800]]
print("Médias por trimestre:", media_por_trimestre(trimestres))

ano_max, ano_min = producao_total_por_ano(dados)
print(f"Ano com maior produção: {ano_max}, menor: {ano_min}")

cultura_max, cultura_min = cultura_maior_menor(dados)
print(f"Cultura com maior produção: {cultura_max}, menor: {cultura_min}")

faz_max, faz_min = fazenda_extremos_por_ano(dados, 2022)
print(f"Fazenda com maior produção: {faz_max}, menor: {faz_min}")

hotel = Hotel()
hotel.adicionar_funcionario("João", "gerente", 5000)
hotel.adicionar_quarto(101, 200)
hotel.reservar_quarto("Maria", 3, 101)
print("Conta final:", hotel.calcular_conta("Maria"))