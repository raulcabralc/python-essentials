n = c = s = ma = me = 0
q = ''
while q in 'SIM':
    n = int(input('Digite um numero: '))
    q = str(input('Deseja continuar? [S/N] ')).upper()
    c += 1
    s += n

    if c == 1:
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
m = s / c
print('Voce digitou {} numeros e a media entre eles foi {:.1f}.'.format(c, m))
print('O maior valor foi {} e o menor foi {}.'.format(ma, me))