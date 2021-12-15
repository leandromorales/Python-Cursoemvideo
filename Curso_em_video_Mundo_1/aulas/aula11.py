#Cores no Terminal:

#  \033[style;text;backm

# Style
# 0 None
# 1 Bold
# 4 Underline
# 7 Negative

# Text
# 30 white
# 31 red
# 32 green
# 33 yellow
# 34 blue
# 35 Magenta
# 36 Ciano
# 37 grey

# Background
# 40 white
# 41 red
# 42 green
# 43 yellow
# 44 blue
# 45 Magenta
# 46 Ciano
# 47 grey

#\033[0;31;41m

#Resetar o padrão do terminal:
#\033[m

print('\033[7;33;44mOlá mundo!\033[m')

nome = 'Teste'

print('Olá. Muito prazer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

