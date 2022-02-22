'''Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

#import just one function from the library "random":
from random import randint

#Starting the lists:
jogo = []
temp = []

#Graphical beggining of the code:
print('-=' * 20)
print(f'{"Jogo da Mega Sena":^37}')

#Variable that gets the attempts of the game:
qt = int(input('Quantos jogos voçê quer que eu sorteie: '))

#First loop to handle the tries of the code:
for g in range(0, qt):
    print(f'{g + 1}º Jogo:', end='')
    #Second loop, to bring up the 6 random tries:
    for c in range(0, 6):
        #Guarantee that the numbers don't repeat itself in the same game attempt:
        while True:
            num = randint(1, 60)
            #if temp.count(num) == 0:
            if num not in temp:
                break
        temp.append(num)
        #print(f'{temp[c]:^5}', end='')
        print(f'{num:^5}', end='')
    #The junction of the both lists in just one multiple list:
    jogo.append(temp[:])
    temp.clear()
    print()
print()

#Extra: Show the result as a multiple list instead of only the print command in the previos loop:
for d in range(0, qt):
    print(f'{d + 1}º Jogo: {jogo[d]}')
print()

#Extra: Show the result as a multiple formatted list:
for i in range(0, qt):
    print(f'{i + 1}º Jogo: ', end='')
    for z in range(0, 6):
        print(f'{jogo[i][z]:^5}', end='')
    print()

#print(jogo)
