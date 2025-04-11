import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = random.choice(l)
u = int(input('Digite um numero inteiro de 1 a 10: '))
while u != c:
    u = int(input('Errou! Tente novamente: '))
print('Voce acertou! O numero era {}!'.format(u))