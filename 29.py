v = int(input('Qual a velocidade do carro (em km/h)? '))
if v > 80:
    m = v - 80
    mv = m * 7
    print('Este carro sera multado em R${}!'.format(mv))
else:
    print('O carro esta dentro do limite de velocidade.')