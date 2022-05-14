'''Crie um código em Python que testes se o site pudim está acessível pelo computador usado.'''


import socket

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.settimeout(.5)
try:
    b = a.connect_ex(('www.pudim.com.br', 80))
    if b == 0:
        print('O site está acessível.')
except:
    print('O site não está acessível.')
a.close()