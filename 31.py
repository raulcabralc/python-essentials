km = int(input('Quantos km voce quer viajar? '))
if km < 200:
    mn = km * 0.5
    print('O valor de sua viagem seria {}'.format(mn))
else:
    ma = km * 0.45
    print('O valor de sua viagem seria {}.'.format(ma))