import os

# Obtendo a lista de arquivos e pastas do diretório atual
lista_arquivos = os.listdir()

# Exibindo cada item individualmente no console
print("Arquivos e pastas no diretório atual:")
for item in lista_arquivos:
    print(item)