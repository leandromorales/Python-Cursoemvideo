'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
uma lista, já na posição correta de inserção (sem usar o sort()).
No final mostre a lista ordenada na tela.'''

#valores = [0, 0, 0, 0, 0]
valores = list()

#Receber 5 valores pelo teclado
for c in range(0, 5):
    num = int(input('Digite um número: '))
    #Jogar o primeiro valor na lista:
    if len(valores) == 0:
        valores.append(num)
        print('Valor adicionado ao final da lista!')
    #Verificar se o número é maior do que os que já existem na lista
    else:
        if num in valores:
            print(f'O número "{num}" já foi digitado nesta sequência')
        else:
            if num > max(valores):
                valores.append(num)
                print('Valor adicionado ao final da lista!')
            if num < min(valores):
                posi = valores.index(min(valores))
                valores.insert(posi - 1, num)
                posii = posi - 1
                print(f'Valor adicionado na posição {posii} da lista!')
print(valores)
