#tplnum = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20)

tplplv = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 
          'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
          'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')

while True:
    n = int(input('Escreva um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('Tente novamente.', end=' ')
print(f'Voce digitou o numero {tplplv[n].capitalize()}.')