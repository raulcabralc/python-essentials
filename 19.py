import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
l = [a1, a2, a3, a4]
s = random.choice(l)
print('O aluno sorteado foi {}.'.format(s))