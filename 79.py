lst = []

while True:

    n = int(input('Digite um numero: '))
    if n in lst:
        print('\033[1;31mValor duplicado! Nao adicionado.\033[m')
    else:
        print(f'\033[1;32mValor {n} adicionado a lista.\033[m')
        lst.append(n)

    dnv = str(input('Voce deseja continuar adicionando? [S/N] ')).upper().strip()
    while dnv not in 'SN':
        dnv = str(input('Voce deseja continuar adicionando? [S/N] ')).upper().strip()
        if dnv == 'S':
            print('', end='')
    if dnv == 'N':
        break

print('-' * 25)
print(f'Voce digitou os valores ', end='')
for c in lst:
    if c != lst[-1]:
        print(f'{c}', end=', ')
    if c == lst[-1]:
        print(f'{lst[-1]}.')