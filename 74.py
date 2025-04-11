import random
tpl = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), 
       random.randint(0, 9), random.randint(0, 9), )

print('Os valores sorteados foram: ', end='')

for n in tpl:
    print(f'{n}', end=' ')

print(f'\nO maior numero foi {max(tpl)}')
print(f'O menor numero foi {min(tpl)}')