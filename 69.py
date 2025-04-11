print('-' * 50)
print(f'{'CADASTRADOR':^50}')
print('-' * 50)

# IMPORT

from time import sleep

# VARIAVEIS

s = 'F'
q = 1
maior = mdi = h = 0

# CADASTRADOR

while True:
    
# IDADE
    
    i = int(input('Qual a sua idade? '))
    if i >= 18:
        maior += 1
    sleep(0.5)
    
# SEXO
    s = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    sleep(0.5)
    while s not in 'MF':
        s = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        mdi += 1
    sleep(0.5)

# CONTINUAR

    n = str(input('Voce gostaria de continuar cadastrando? [S/N] ')).strip().upper()[0]
    sleep(0.35)
    while n not in 'SN':
        n = str(input('Voce gostaria de continuar cadastrando? [S/N] ')).strip().upper()[0]
        sleep(0.35)
    if n == 'S':
        print('\nContinuando programa...\n')
        sleep(0.2)
    if n == 'N':
        break

# FINAL

print(f'\nVoce cadastrou {maior} maiores de idade')
sleep(0.1)
print(f'Voce cadastrou {h} homens')
sleep(0.1)
print(f'Voce cadastrou {mdi} mulheres abaixo de 20 anos')
sleep(2)
print('Encerrando programa...')
sleep(2)