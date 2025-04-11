n = int(input('Escreva um numero inteiro: '))
p = n % 1 == 0 and n % n == 0 and n % 2 != 0
if p == True:
    print('Este numero e primo!')
else:
    print('Este numero nao e primo!')