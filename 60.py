n = int(input('Digite um numero: '))
m = n
mult = 1
print('Calculando {}! = '.format(n), end='')
while m != 0:
    print('{}'.format(m), end='')
    print(' x ' if m > 1 else ' = ', end='')
    mult *= m
    m -= 1
print(mult)