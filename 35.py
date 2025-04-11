l1 = int(input('Digite a medida do primeiro lado do triangulo: '))
l2 = int(input('Digite a segunda medida: '))
l3 = int(input('Digite a terceira medida: '))
t = l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2
if t == True:
    print('Este triangulo existe.')
else:
    print('Este triangulo nao existe.')