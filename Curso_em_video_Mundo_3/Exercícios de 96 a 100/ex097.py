'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável.
'''

def escreva(entrada):
    guia = len(entrada)
    print('~' * guia)
    print(entrada)
    print('~' * guia)


frase1 = str(' Teste ')
frase2 = str(' Esquistossomose ')

escreva(frase1)
escreva(frase2)