import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
l = [a1, a2, a3, a4]
s = random.shuffle(l)
print('A ordem de escolha sera: ')
print(l)