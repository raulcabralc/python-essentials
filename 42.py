l1 = int(input('Digite o primeiro lado do triangulo: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
t = l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1
if t == True:
    if l1 == l2 == l3:
        print('Este triangulo e equilatero.')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Este triangulo e isosceles.')
    elif l1 != l2 != l3:
        print('Este triangulo e escaleno.')
else:
    print('Este triangulo nao existe.')