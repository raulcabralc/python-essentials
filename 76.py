lst = ('X-Burger', 14.50, 
       'X-Egg', 16.50, 
       'X-Bacon', 16.50, 
       'X-BaconEgg', 18.00, 
       'X-Tudo', 20.00, 
       'X-Monstro', 24.50)

print('-' * 37)
print(f'{'CARDAPIO':^37}')
print('-' * 37)

for pos in range(0, len(lst)):
    if pos % 2 == 0:
        print(f'{lst[pos]:.<30}', end='')
        print(f'R$ {lst[pos+1]}')
print('-' * 37)