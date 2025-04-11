from time import sleep
print('=' * 50)
print(' ' * 11, '10 PRIMEIROS TERMOS DA PA')
print('=' * 50)
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
p = 0
while p < 10:
    print(' {} '.format(t), end=(' ➝ '))
    p += 1
    t+= r
print('  FIM')