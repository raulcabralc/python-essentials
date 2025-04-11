s = t = c = 0
while t != 999:
    t = int(input('Digite um numero para a soma [999 para encerrar] '))
    s += t
    c += 1
print('A soma desses {} numeros foi de {}.'.format(c, s - 999))