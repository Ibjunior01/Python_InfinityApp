from dados import dados_producao
from funcoes import (
    producao_por_ano,
    producao_por_cultura,
    producao_por_fazenda_em_ano
)

# Análise por ano
ano_max, prod_max, ano_min, prod_min = producao_por_ano(dados_producao)
print(f"Ano com maior produção: {ano_max} ({prod_max})")
print(f"Ano com menor produção: {ano_min} ({prod_min})")

# Análise por cultura
cultura_max, val_max, cultura_min, val_min = producao_por_cultura(dados_producao)
print(f"Cultura com maior produção: {cultura_max} ({val_max})")
print(f"Cultura com menor produção: {cultura_min} ({val_min})")

# Análise por fazenda em ano específico
ano_escolhido = 2022
faz_max, val_fmax, faz_min, val_fmin = producao_por_fazenda_em_ano(dados_producao, ano_escolhido)
print(f"No ano {ano_escolhido}, fazenda com maior produção: {faz_max} ({val_fmax})")
print(f"No ano {ano_escolhido}, fazenda com menor produção: {faz_min} ({val_fmin})")