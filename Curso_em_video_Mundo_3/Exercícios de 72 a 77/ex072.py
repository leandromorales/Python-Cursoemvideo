#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
#até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


nums = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
        'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

ent = int(input('Digite um número entre 0 e 20: '))

while ent not in range(0, 21):
    ent = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {nums[ent]}')
print('Fim')