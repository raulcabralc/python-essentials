from time import sleep
print('=' * 50)
print(' ' * 11, '10 PRIMEIROS TERMOS DA PA')
print('=' * 50)
a1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva a razao da PA: '))
d = a1 + (10 - 1) * r
for c in range(a1, d, r):
    print(' {} '.format(c), end=' ➝ ')
print('  FIM')


#n = 10
#an = a1 + (n - 1) * r