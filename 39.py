n = int(input('Que ano voce nasceu? '))
i = 2024 - n
if n > 2024:
    print('Voce esta pra nascer ou veio do futuro.')

if i < 18:
    print('Voce ainda nao precisa se alistar.')
    f = i - 18
    ff = f * -1
    print('Faltam {} ano(s) para voce se alistar.'.format(ff))
elif i == 18:
    print('Voce tem que se alistar esse ano.')
elif i > 18:
    print('Voce ja se alistou ou ja passou do prazo.')
    f = i - 18
    print('Se passaram {} ano(s) que ocorreu o seu alistamento (caso tenha se alistado).'.format(f))