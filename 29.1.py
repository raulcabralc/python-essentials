s = int(input('Quantos km o carro andou? '))
t = float(input('Em quantas horas ele chegou? '))
v = s / t
if v > 80:
    print('O carro sera multado!')
else:
    print('O carro nao sera multado.')