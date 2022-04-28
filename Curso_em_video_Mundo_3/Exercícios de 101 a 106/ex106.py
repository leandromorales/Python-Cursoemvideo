'''Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra "FIM" o programa se encerrará.

OBS: use cores.'''


from time import sleep


while True:
    ch = str(input('Função ou Biblioteca> ')).lower()
    if ch in 'end':
        break
    print('~' * 30)
    print(f"Acessando o manual do comando '{ch}'")
    print('~' * 30)
    sleep(1)
    help(f'{ch}')

print('~' * 10)
print('ATÉ LOGO!')
print('~' * 10)