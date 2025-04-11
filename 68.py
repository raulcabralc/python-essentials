print('-' * 50)
print('{:^50}'.format('PAR OU IMPAR'))
print('-' * 50)

# IMPORT

import random
from time import sleep

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cont = 0

# CRIANDO O JOGO

while True:

    pi = str(input('Escolha entre par ou impar: ')).upper().strip()
    n = int(input('Escolha um numero de 0 a 10: '))
    c = random.choice(lst)
    sleep(1)
    
    s = (n + c) % 2 == 0
    sa = n + c

# ESCOLHEU PAR

    if pi == 'PAR' and s == True:
        print(f'Voce venceu! O computador escolheu {c}. O resultado final foi {sa}, assim sendo um resultado PAR!')
        cont += 1
    if pi == 'PAR' and s == False:
        print(f'Voce perdeu... O computador escolheu {c}. O resultado final foi {sa}, assim sendo um resultado IMPAR!')
        break

# ESCOLHEU IMPAR

    if pi == 'IMPAR' and s == True:
        print(f'Voce perdeu... O computador escolheu {c}. O resultado final foi {sa}, assim sendo um resultado PAR!')
        break
    if pi == 'IMPAR' and s == False:
        print(f'Voce venceu! O computador escolheu {c}. O resultado final foi {sa}, assim sendo um resultado IMPAR!')
        cont += 1

print(f'\nVoce venceu {cont} vezes seguidas antes de perder!')
sleep(1)
print('\nFIM DE JOGO!!')


