nome = input('Qual é o seu nome? ')
#20 Caracteres alinhado à esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
#20 Caracteres alinhado à direita
print('Prazer em te conhecer {:>20}!'.format(nome))
#20 Caracteres alinhado no centro
print('Prazer em te conhecer {:^20}!'.format(nome))
#Print sem quebra de linha
print('Prazer em te conhecer ', end='')
print('Tentando acertar.')
#Quebra de linha no print
print('Prazer em te conhecer \nleandro' )
