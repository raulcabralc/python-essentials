print('Confirmacao para realizacao do emprestimo.\n')
v = float(input('Qual o valor da casa em reais? '))
s = float(input('Qual o seu salario? '))
a = int(input('Em quantos anos voce ira parcelar esta compra? '))
p = v / a
if p > 1.3 * s:
    print('Voce nao pode realizar este emprestimo.')
else:
    print('Voce pode realizar este emprestimo.')