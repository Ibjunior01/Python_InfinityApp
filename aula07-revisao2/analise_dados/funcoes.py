def producao_por_ano(dados):
    totais = {}
    for registro in dados:
        ano = registro['ano']
        total = registro['milho'] + registro['soja'] + registro['trigo']
        totais[ano] = totais.get(ano, 0) + total
    ano_max = max(totais, key=totais.get)
    ano_min = min(totais, key=totais.get)
    return ano_max, totais[ano_max], ano_min, totais[ano_min]

def producao_por_cultura(dados):
    culturas = {'milho': 0, 'soja': 0, 'trigo': 0}
    for registro in dados:
        for cultura in culturas:
            culturas[cultura] += registro[cultura]
    cultura_max = max(culturas, key=culturas.get)
    cultura_min = min(culturas, key=culturas.get)
    return cultura_max, culturas[cultura_max], cultura_min, culturas[cultura_min]

def producao_por_fazenda_em_ano(dados, ano_escolhido):
    fazendas = {}
    for registro in dados:
        if registro['ano'] == ano_escolhido:
            total = registro['milho'] + registro['soja'] + registro['trigo']
            fazendas[registro['fazenda']] = total
    fazenda_max = max(fazendas, key=fazendas.get)
    fazenda_min = min(fazendas, key=fazendas.get)
    return fazenda_max, fazendas[fazenda_max], fazenda_min, fazendas[fazenda_min]