'''Crie um código em Python que testes se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
    #print(site.read())
