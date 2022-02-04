'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
uma lista, já na posição correta de inserção (sem usar o sort()).
No final mostre a lista ordenada na tela.'''


valores = list()

for c in range(0, 5):
    num = int(input('Digite um número: '))
    if len(valores) == 0:
        valores.append(num)
        print('NNúmero adicionado ao final da lista.')
    elif num in valores:
        print('Este número já foi digitado.')
    else:
        if num > max(valores):
            valores.append(num)
            print('Número adicionado ao final da lista.')
        if num < min(valores):
            pos = valores.index(min(valores))
            print(f'Valor adicionado na posição {pos}.')
            valores.insert(pos, num)
        if len(valores) >= 2:
            if num > valores[0] and num < valores[1]:
                print(f'Valor adicionado na posição {1}.')
                valores.insert(1, num)
        if len(valores) >= 3:
            if num > valores[1] and num < valores[2]:
                print(f'Valor adicionado na posição {2}.')
                valores.insert(2, num)
        if len(valores) >= 4:
            if num > valores[2] and num < valores[3]:
                print(f'Valor adicionado na posição {3}.')
                valores.insert(3, num)
        if len(valores) >= 5:
            if num > valores[3] and num < valores[4]:
                print(f'Valor adicionado na posição {4}.')
                valores.insert(4, num)

print(valores)