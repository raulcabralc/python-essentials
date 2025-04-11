from time import sleep

print('-' * 50)
print(' ' * 18, 'TABUADAS')
print('-' * 50)

c = 0

# while n >= 0: PODERIA SER, MAS TEM QUE FAZER COM O BREAK NESSE EXERCICIO

while True:

    print('Caso queira encerrar o programa, digite um numero negativo.')
    n = int(input('Escreva um numero: '))
    sleep(0.5)
    
    print('-' * 15)
    
    c = 0

    if n < 0:
        break

    while c <= 10:
        r = n * c
        sleep(0.1)
        print(f'{n} x {c} = {r}')
        c += 1
    print('-' * 15)
    sleep(0.5)
print('Encerrando programa...')
sleep(1)