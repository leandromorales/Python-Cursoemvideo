#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
dob = num * 2
trip = num * 3
raiz = num ** (0.5)
print('O dobro de {} é igual a {}. '.format(num, dob))
print('O triplo de {} é igual a {}.'.format(num, trip))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, raiz))
