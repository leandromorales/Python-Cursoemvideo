# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

seq = int(input('Digite a quantidade de elementos da sequencia: ')) + 1
cont = 1
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
while cont != seq:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' FIM')
