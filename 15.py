km = float(input('Quantos km esse carro ja rodou? '))
dia = int(input('Quantos dias voce usou o carro? '))
p = (dia*60)+(km*0.15)
print('O total a se pagar seria {:.2f} reais.'.format(p))