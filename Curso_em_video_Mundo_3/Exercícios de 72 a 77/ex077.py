'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('teste', 'deveres', 'tentativa', 'erro', 'perseverança', 'resiliencia',
'curso', 'malta')

for g in range(0, len(palavras)):
    palavra = palavras[g]
    print(f'\nAs vogais da palavra "{palavra}" são: ', end='')
    for c in range(0, len(palavra)):
        if palavra[c] in 'aeiou':
            print(palavra[c], end='')