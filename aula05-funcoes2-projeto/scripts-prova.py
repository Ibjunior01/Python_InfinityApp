# processador_texto.py

def processador_texto(texto, **kwargs):
    resultado = texto

    operacoes = {
        'contar_palavras': lambda t: print(f" Palavras: {len(t.split())}"),
        'contar_letras': lambda t: print(f" Letras: {len(t.replace(' ', ''))}"),
        'inverter_texto': lambda t: t[::-1],
        'substituir_palavra': lambda t: t.replace(kwargs.get('substituir_palavra', ''), kwargs.get('nova_palavra', ''))
    }

    for chave in kwargs:
        if chave in operacoes:
            operacao = operacoes[chave]
            if chave in ['inverter_texto', 'substituir_palavra']:
                resultado = operacao(resultado)
            else:
                operacao(resultado)

    return resultado

# Exemplo de uso
if __name__ == "__main__":
    texto = "Python é incrível e Python é versátil"
    resultado = processador_texto(
        texto,
        contar_palavras=True,
        contar_letras=True,
        inverter_texto=True,
        substituir_palavra="Python",
        nova_palavra="JavaScript"
    )
    print(" Texto final:", resultado)