contato = {}
contato['nome'] = input('Insira o nome do contato: ')
contato['telefone'] = input('Insira o número de telefone do contato: ')
contato['email'] = input('Insira o email do contato: ')

print('\nInformações do contato: ')
for chave, valor in contato.items():
    print(f'{chave.capitalize()}: {valor}')