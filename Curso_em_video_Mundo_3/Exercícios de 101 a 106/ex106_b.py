'''Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra "FIM" o programa se encerrará.

OBS: use cores.'''


def display(msg, color):
    from time import sleep
    t = len(msg) + 4
    print(f'\033[1;30;{color}m~\033[m' * t)
    print(f'\033[1;30;{color}m  {msg}  \033[m')
    print(f'\033[1;30;{color}m~\033[m' * t)
    sleep(1)

while True:
    display('SISTEMA DE AJUDA PYHELP', 42)
    ch = str(input('Função ou Biblioteca> ')).lower()
    if ch in 'fim':
        break
    display(f"Acessando o manual do comando '{ch}'", 44)
    help(f'{ch}')
display('ATÉ LOGO!', 41)
