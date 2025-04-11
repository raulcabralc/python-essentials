print('-=-' * 10)
print(f'{'BANCO':^30}')
print('-=-' * 10)

# CEDULAS

ced = 50
totced = 0

# SACAR

v = int(input('Que valor voce quer sacar? R$'))
t = v

# INICIO

while True:
    if t >= ced:
        t -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Voce sacou {totced} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if t == 0:
            break