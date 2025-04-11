import random
l = [0, 1, 2, 3, 4, 5]
a = random.choice(l)
r = int(input('Adivinhe um numero inteiro de 0 a 5: '))
if a == r:
    print('Voce adivinhou o numero correto!')
else:
    print('Voce errou o numero!')