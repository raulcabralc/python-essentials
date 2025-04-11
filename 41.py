print('Bem-vindo(a) a Confederacao Nacional de Natacao.')
n = int(input('Qual o seu ano de nascimento? '))
i = 2024 - n
if i <= 9:
    print('Sua categoria e a MIRIM.')
elif i <= 14:
    print('Sua categoria e a INFANTIL.')
elif i <= 19:
    print('Sua categoria e a JUNIOR.')
elif i == 20:
    print('Sua categoria e a SENIOR.')
elif i > 20:
    print('Sua categoria e a MASTER.')