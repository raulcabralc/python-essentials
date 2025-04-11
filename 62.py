from time import sleep
print('=' * 50)
print(' ' * 12, 'GERADOR DE TERMOS DA PA')
print('=' * 50)
t = int(input('Digite o primeiro termo: '))
sleep(0.05)
r = int(input('Digite a razao: '))
sleep(0.05)
te = t
p = 1
tt = 0
m = 5
while m != 0:
    tt += m
    while p <= tt:
        print('\033[1;32m {} \033[m'.format(te), end=('  ➝ '))
        te += r
        p += 1
    print('  PAUSA')
    print('Caso queira parar, digite \033[1;31m0\033[m.')
    m = int(input('Quantos termos voce quer mostrar a mais? '))
    sleep(0.2)
print('\033[1;31mEncerrando programa...\033[m')
sleep(1.5)