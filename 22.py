n = input('Qual o seu nome completo? ')
print('Seu nome em letras maiusculas e {}.'.format(n.upper()))
print('Seu nome em letras minusculas e {}.'.format(n.lower()))
ns = n.replace(' ', '')
print('Seu nome completo tem {} letras.'.format(len(ns)))
np = n.split()
print('Seu primeiro nome tem {} letras.'.format(len(np[0])))