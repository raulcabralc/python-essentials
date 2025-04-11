n = int(input('Digite um numero inteiro: '))
r = n % 2
if r == 0:
    print('O numero {} e Par!'.format(n))
else:
    print('O numero {} e Impar!'.format(n))