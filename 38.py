n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
if n1 > n2:
    print('O numero {} e maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('O numero {} e maior que {}.'.format(n2, n1))
elif n1 == n2:
    print('Os dois numeros sao iguais, sendo eles {}.'.format(n1))