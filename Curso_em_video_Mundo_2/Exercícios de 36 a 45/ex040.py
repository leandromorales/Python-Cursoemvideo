#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# - Média abaixo de 5.0: Reprovado;
# - Média entre 5.0 e 6.9: Recuperação;
# - Média 7.0 ou superior: Aprovado.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('O aluno foi reprovado com média {:.1f}.'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('O aluno está em recuperação com média {:.1f}'.format(media))
else:
    print('O aluno foi aprovado com média {:.1f}'.format(media))