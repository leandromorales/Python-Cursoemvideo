#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido.
#import random
from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

#sort = random.choice([aluno1, aluno2, aluno3, aluno4])
sort = choice([aluno1, aluno2, aluno3, aluno4])
print('O nome do aluno sorteado foi: {}.'.format(sort))
