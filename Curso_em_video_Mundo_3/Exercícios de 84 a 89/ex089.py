'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta. No final, mostre um boletim contendo a média de cada um e permita que o
usuário possa mostrar as notas de cada aluno individualmente.'''

notas = []
temp = []
boletim = []
ch = ''
while True:
    temp.append(str(input('Digite o nome do aluno: ')))
    temp.append(float(input('Digite a primeira nota: ')))
    temp.append(float(input('Digite a segunda nota: ')))
    notas.append(temp[:])
    temp.clear()
    dec = str(input('Deseja continuar? [S/N] '))
    if dec in 'Nn':
        break
#print(notas)
print('-=' * 30)
print(f'{"No.":<6}{"Nome":<10}{"Média":^15}')
print('-' * 30)
for c in range(0, len(notas)):
    print(f'{c:<6}{notas[c][0]:<10}{(notas[c][1] + notas[c][2]) / 2:^15.1f}')

while True:
    ch = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if ch == 999:
        break
    print(f'Notas de {notas[ch][0]} são [{notas[ch][1]}, {notas[ch][2]}]')
print('O programa será encerrado.')