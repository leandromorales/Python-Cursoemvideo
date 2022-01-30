'''Aula 17 - Listas'''

#Criar lista
num = [2,5,9,1]

#Alterar um valor da lista
num[2] = 3

#Adicionar um valor na lista
num.append(7)

#Organizar os itens da lista
num.sort(reverse = True)

#Inserir elemento no índice 2
num.insert(2, 0)

#Remover o caracter na posição 2
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.\n')

print('-' * 30)

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-' * 30)

values = list()
for cont in range(0, 5):
    values.append(int(input('Digite um valor: ')))

for c, v in enumerate(values):
    print(f'Na posição {c} encontrei o valor {v}!')

print('-' * 30)

#Ligação entre listas
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a};')
print(f'Lista B: {b}.')

print('-' * 30)

#Cópia de listas

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a};')
print(f'Lista B: {b}.')

print('-' * 30)

#Mostrar posição de um caracter em uma lista:
#valores.index(5))
#valores.index(max(valores))

#Max and Min values in a list:
#max(valores)
#min(valores)