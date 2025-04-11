lst = []

while True:
    n = int(input('Digite um numero: '))
    lst.append(n)

    dnv = str(input('Voce deseja continuar? [S/N] ')).upper().strip()
    while dnv not in 'SN':
        print('Resposta invalida.', end=' ')
        dnv = str(input('Voce deseja continuar? [S/N] ')).upper().strip()
    if dnv == 'S':
        ...
    if dnv == 'N':
        break
print(f'A lista possui {len(lst)} valores')
lst.sort(reverse=True)
print(f'A lista em ordem decrescente seria {lst}')
print('O valor 5 esta na lista' if 5 in lst else 'O valor 5 nao esta na lista')