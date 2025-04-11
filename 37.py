n = int(input('Digite um numero inteiro: '))
print('Escolha uma opcao para realizar a conversao do numero acima:')
print('[ 1 ] Converter para BINARIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL')
e = int(input('Escolha: '))
if e == 1:
    print('{} convertido para binario seria {}.'.format(n, bin(n)[2:]))
elif e == 2:
    print('{} convertido para octal seria {}.'.format(n, oct(n)[2:]))
elif e == 3:
    print('{} convertido para hexadecimal seria {}.'.format(n, hex(n)[2:]))
else:
    print('Escolha um numero de 1 a 3!')