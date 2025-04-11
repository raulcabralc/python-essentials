n = str(input('Qual o seu nome? ')).strip().split()
print('Seu primeiro nome e {}.'.format(n[0]))
print('Seu ultimo nome e {}.'.format(n[len(n)-1]))