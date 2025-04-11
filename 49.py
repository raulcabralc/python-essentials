from time import sleep
n = int(input('Escolha um numero para verificar sua tabuada: '))
print('A tabuada deste numero seria:')
for c in range(n, n * 10 + 1, n):
    print(c)
    sleep(0.1)