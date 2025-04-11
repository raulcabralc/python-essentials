n = input('Qual o seu nome? ').strip()
na = 'silva' in n.lower()
if na == True:
    print('Seu nome tem Silva.')
else:
    print('Seu nome nao tem Silva.')
#print('Seu nome tem Silva? {}'.format('silva' in n.lower()))
#nn = str(n.upper)
#nnn = (nn.find('SILVA'))
#print(nnn)