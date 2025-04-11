s = float(input('Qual o seu salario? '))
if s > 1250:
    a1 = s * 1.1
    print('Seu novo salario com um aumento de 10% seria de {:.2f} reais.'.format(a1))
else:
    a2 = s * 1.15
    print('Seu novo salario com um aumento de 15% seria de {:.2f} reais.'.format(a2))