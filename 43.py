p = float(input('Qual o seu peso (em kg)? '))
a = float(input('Qual a sua altura (em metros)? '))
imc = p / a ** 2
print('Seu IMC e de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif imc < 25:
    print('Voce esta no peso ideal.')
elif imc < 30:
    print('Voce esta em sobrepeso.')
elif imc < 40:
    print('Voce esta obeso.')
elif imc > 40:
    print('Voce esta em obesidade morbida.')