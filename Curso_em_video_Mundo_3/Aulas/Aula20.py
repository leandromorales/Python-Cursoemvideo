'''Aula 20: Funções parte 1'''

def mostraLinha():
    print('-------------------------')

mostraLinha()
print('   SISTEMA DE ALUNOS   ')
mostraLinha()
mostraLinha()
print('   CADASTRO DE FUNCIONÁRIOS   ')
mostraLinha()
mostraLinha()
print('   TESTE   ')
mostraLinha()

def lin():
    print('-' * 30)

lin()
print('   CURSO EM VÍDEO   ')
lin()
print('   APRENDA PYTHON   ')
lin()
print('   GUSTAVO GUANABARA   ')
lin()


def título(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


título('SISTEMA DE ALUNOS')
título('CURSO DE PYTHON')
título('TENTANDO')

a = 4
b = 5
soma = a + b


def somar(a, b):
    s = a + b
    print(f'A soma A + B é igual a {s}.')


somar(4, 5)
somar(8, 9)
somar(2, 1)
somar(b=4, a=5)

#Empacotar parâmetros

def contador(* me):
    for valor in me:
        print(f' {valor} ', end='')
    print()
    print(f'Recebi os valores {me} e são ao todo {len(me)} números.')
    print('FIM!')
    print()



contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def somare(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


somare(5, 2)
somare(2, 9, 4)

