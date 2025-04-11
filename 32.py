a = int(input('Em que ano estamos? '))
b = a % 4
if b == 0:
    print('Estamos em um ano bissexto!')
else:
    print('Nao estamos em um ano bissexto!')