p = float(input('Quantos reais e o produto a ser pago? '))
print('Lista de metodos de pagamento: ')
print('[ 1 ] A vista em dinheiro ou cheque')
print('[ 2 ] A vista no cartao')
print('[ 3 ] Parcelado em 2 vezes no cartao')
print('[ 4 ] Parcelado em 3 vezes no cartao')
e = int(input('Escolha o metodo de pagamento: '))
if e == 1:
    d = p * 0.9
    print('O valor do produto com um desconto de 10% sera de {} reais.'.format(d))
elif e == 2:
    c = p * 0.95
    print('O valor do produto com um desconto de 5% sera de {} reais.'.format(c))
elif e == 3:
    print('O valor do produto nao ira alterar, permanecendo em {} reais.'.format(p))
elif e == 4:
    c3 = p * 1.2
    print('O valor do produto com juros de 20% sera de {} reais.'.format(c3))
else:
    print('Escolha uma das opcoes acima, entre 1 e 4.')