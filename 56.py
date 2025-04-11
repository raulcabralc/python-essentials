from time import sleep
si = 0
m = 0
mh = 0
nv = ''
tm = 0
for p in range(1,5):
    print('----- {} PESSOA -----'.format(p))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    g = str(input('Genero (M/F): ')).strip()
    si += i
    if p == 1 and g in 'Mm':
        mh = i
        nv = n
    if g in 'Mm' and i > mh:
        mh = i
        nv = n
    if g in 'Ff' and i < 20:
        tm += 1
m = si/4
sleep(0.4)
print('\nA media das idades deste grupo e de \033[1;33m{}\033[m anos.'.format(m))
sleep(0.1)
print('\nO homem mais velho seria o \033[1;33m{}\033[m e ele tem \033[1;33m{}\033[m anos.'.format(nv, mh))
sleep(0.1)
print('\nExistem \033[1;33m{}\033[m mulheres com menos de 20 anos neste grupo.'.format(tm))