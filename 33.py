n1 = float(input('Escreva um numero: '))
n2 = float(input('Escreva outro numero: '))
n3 = float(input('Escreva mais um numero: '))
l = [n1, n2, n3]
# ACHANDO O MENOR
if n1 < n2 and n1 < n3:
    mn = n1
if n2 < n1 and n2 < n3:
    mn = n2
if n3 < n1 and n3 < n2:
    mn = n3
# ACHANDO O MAIOR
if n1 > n2 and n1 > n3:
    ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('O maior numero seria o {} e o menor seria o {}.'.format(ma, mn))