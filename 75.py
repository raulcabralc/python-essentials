n = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), 
     int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Voce digitou os numeros {n}')
print(f'O numero 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O numero 3 apareceu na posicao {n.index(3) + 1}')
else:
    print('O numero 3 nao apareceu nesta lista')
print('Os numeros pares desta lista foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')