#Condições aninhadas

nome = str(input('Qual é o seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')

print('Tenha um bom dia, {}!'.format(nome))