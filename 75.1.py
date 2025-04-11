# TENTATIVA QUE FOI MUITO ERRADA KKKKKKK

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
tpl = (n1, n2, n3, n4)

c = p1 = p2 = p3 = p4 = 0

if n1 % 2 == 0:
    c += 1
    n1 = p1
if n2 % 2 == 0:
    c += 1
    n2 = p2
if n3 % 2 == 0:
    c += 1
    n3 = p3
if n4 % 2 == 0:
    c += 1
    n4 = p4

a = tpl.count(9)

if 3 in tpl:
    b = tpl.index(3) + 1

print(f'\nVoce digitou os valores {tpl}')
print(f'Tivemos {a} numeros 9 nesta lista')
if 3 in tpl:
    print(f'O numero tres estava na posicao {b}')
else:
    print('Nao tivemos numero 3 nesta lista')
print(f'Tivemos {c} numeros pares nesta lista, sendo eles {p1}, {p2}, {p3}, {p4}.')