lst = []
lstp = []
lsti = []
while True:
    n = int(input('Escreva um valor: '))
    lst.append(n)
    if n % 2 == 0:
        lstp.append(n)
    if n % 2 != 0:
        lsti.append(n)

    dnv = str(input('Voce quer continuar? [S/N] ')).strip().upper()
    while dnv not in 'SN':
        print('Resposta invalida.', end=' ')
        dnv = str(input('Voce quer continuar? [S/N] ')).strip().upper()
    if dnv in 'N' and not 'SIN':
        break
print(f'A lista foi {lst}')
print(f'Os numeros pares dessa lista foram {lstp}')
print(f'Os numeros impares dessa lista foram {lsti}')