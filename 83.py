e = str(input('Digite a expressao: '))
c = e.count('(') + e.count(')')
if c % 2 == 0:
    print('Os parenteses estao na quantidade certa!')
else:
    print('Os parenteses nao estao na quantidade certa!')
# O CODIGO NAO RECONHECE SE O ) VEM ANTES OU DEPOIS
# DO ( E VICE VERSA