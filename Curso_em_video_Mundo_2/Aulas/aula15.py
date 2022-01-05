# Aula 15 - Interrompendo repetições while

# Prática:

#  Loop infinito:
# cont = 1
# while True:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou')
#

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
# Usando Fstrings
print(f'A soma vale {s}')


# nome = 'José'
# idade = 33
# print(f'O {nome} tem {idade} anos.') #Python 3.6+
# print('O {} tem {} anos.'.format(nome, idade)) # Python 3
# print('O %s tem %d anos' % (nome, idade)) # Python 2

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}')

