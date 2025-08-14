from datetime import datetime

def validar_data(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        return None

def formatar_nome(nome):
    return nome.strip().title()