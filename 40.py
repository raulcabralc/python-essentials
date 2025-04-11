n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A media do aluno foi de {}.'.format(m))
if m >= 7:
    print('O aluno foi aprovado.')
elif m < 7 and m >= 5:
    print('O aluno precisara de recuperacao.')
elif m < 5:
    print('O aluno foi reprovado.')