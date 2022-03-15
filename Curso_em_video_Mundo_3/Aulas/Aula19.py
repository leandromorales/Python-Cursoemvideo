'''Dicionários em Python'''

'''To declare dictionaries:
dados=dict()
dados={}'''

'''To create items:
dados['idade']='25' '''

'''To remove an item(key and value):
del dados['idade']'''

filme = {'titulo':'Star Wars',
         'ano':'1977',
         'diretor':'George Lucas'
    }

print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

#Use in loops:
for k, v in filme.items():
    print(f'O {k} é {v}.')
print()
for a, b in filme.items():
    print(f'O {a} é {b}.')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print()
print(pessoas['nome'])
print()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())

for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
#Dictionaries inside lists:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

print()
state = dict()
br = list()
for c in range(0, 3):
    state['uf'] = str(input('Unidade Federativa: '))
    state['sigla'] = str(input('Sigla: '))
    br.append(state.copy())
for e in br:
    for v in e.values():
        print(v, end=' ')
    print()