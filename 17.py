co = float(input('Qual o valor do cateto oposto do triangulo? '))
ca = float(input('E qual o valor do cateto adjacente? '))
hq = co**2 + ca**2
h = hq**(1/2)
print('O valor da hipotenusa deste triangulo retangulo seria {:.1f}.'.format(h))