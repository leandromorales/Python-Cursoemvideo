'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:

- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional).

Adicione também as docstrings da função.'''

def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''

    soma = maior = menor = 0
    a = len(n)
    for c, d in enumerate(n):
        soma += d
        if c == 0:
            maior = menor = d
        if d > maior:
            maior = d
        if d < menor:
            menor = d

    result = {'total' : a, 'maior': maior, 'menor' : menor, 'média' : float(f'{soma / a:.2f}')}
    if sit:
        if result['média'] <= 4:
            result['situação'] = 'RUIM'
        elif 4.1 <= result['média'] <= 7:
            result['situação'] = 'RAZOÁVEL'
        else:
            result['situação'] = 'BOA'

    return (result)


#Programa principal
resp = notas(5.5, 9.5, 10.5, 6.5, sit=True)
print(resp)
