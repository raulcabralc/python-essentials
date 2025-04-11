print('-' * 50)
print(f'{'LEITOR DE PRODUTOS':^50}')
print('-' * 50)

# IMPORT

from time import sleep

# VARIAVEIS

t = caro = ma = me = c = 0
nb = ''
mn = ''

# LEITOR

while True:

    c += 1
    sleep(0.3)

# NOME

    print('-' * 20)
    n = str(input('Qual o nome desse produto? '))
    sleep(0.5)
    print('-' * 20)
    mn = n

# PRECO

    p = float(input('Qual o preco desse produto? '))
    sleep(0.5)
    print('-' * 20)
    t += p
    if p > 1000:
        caro += 1
    
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
            me = mn

# CONTINUAR

    dnv = input('Voce gostaria de continuar lendo produtos? [S/N] ').upper().strip()[0]
    if dnv == 'S':
        print('-' * 20)
    if dnv == 'N':
        break
print(f'\nO total gasto nesses produtos foi de R${t}')
sleep(0.35)
print(f'{caro} produtos nessa lista custaram mais de R$1000,00')
sleep(0.35)
print(f'O produto mais barato foi {mn} e custou {me}')
sleep(2)
print('\nEncerrando programa...')
sleep(2)