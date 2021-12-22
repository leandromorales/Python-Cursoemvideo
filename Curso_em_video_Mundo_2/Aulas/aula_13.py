#Laço de repetição FOR

print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')

for c in range(1, 6):
    print('Tchau')
    print(c)
print('fim - Contagem de 1 a 5')

#Laço decrescente:
for c in range(6, 0, -1):
    print('Tchau')
    print(c)
print('fim - Contagem de 5 a 1')

#Definir intervalo e passo:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

#Somatório de valores digitados:

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
    #s = s + n
print('O somatório dos valores é: {}'.format(s))