'''Aula 21

Interactive Help
Docstrings
Argumentos opcionais
Escopo de variáveis
Retorno de resultados'''

'''Interactive Help

help() = Internal function or method where we can get a manual of every function in Python.'''
'''Example:

help> print
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

help> quit
'''

'''Docstrings: Documents to explain functions made by the users.

'''

def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    Função criada por Gustavo Guanabara do canal CursoemVídeo.'''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

help(contador)

'''Argumentos opcionais: When you don't know if every parameter will be used, you can add "=0". In case the function call
don't send that parameter, it won't return an error.

'''

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)

def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

soma(8, 4, 6)
soma()

'''Escopo de variáveis: place where the variable will exists or not.'''
'''
Global Scope: if a variable is declared in global scope, it'll run in every function.
Local Scope: if a variable is declared only in local scope, it'll run only within the local function.
'''

def funcao():
    n1 = 4
    print(f'N1 local vale {n1}')

n1 = 2
funcao()
print(f'N1 global vale {n1}')


def funcaoo():
    global nn1
    nn1 = 4
    print(f'NN1 local vale {nn1}')

nn1 = 2
funcaoo()
print(f'NN1 global vale {nn1}')

def somare(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somare(3, 2, 5)
r2 = somare(2, 2)
r3 = somare(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
