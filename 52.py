n = int(input('Digite um numero inteiro: '))
t = 0
for c in range(1, n + 1):
    p1 = n % c == 0
    if p1 == True:
        print('\033[32m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
    # SE APENAS DOIS NUMEROS FOREM DIVISIVEIS NESSE RANGE O NUMERO E PRIMO
print('\033[m\nO numero \033[1;33m{}\033[m e divisivel por \033[1;33m{}\033[m numeros'.format(n, t))
if t == 2:
    print('Sendo assim, um numero primo.')
else:
    print('Sendo assim, um numero nao primo.')