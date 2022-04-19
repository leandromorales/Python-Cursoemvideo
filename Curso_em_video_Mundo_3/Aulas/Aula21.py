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

#27:56