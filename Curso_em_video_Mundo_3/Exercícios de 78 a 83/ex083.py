'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.'''


valores = str(input('Digite uma expressão: '))
#print(valores)
if valores.count('(') == valores.count(')'):
    print('A expressão digitada é válida.')
else:
    print('A expressão digitada é inválida.')
