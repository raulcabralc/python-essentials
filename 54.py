coram = '\033[1;33m'
corpa = '\033[m'
a = 0
s = 1
ma = 0
me = 0
for c in range(1, 8):
    n = int(input('Em que ano a {} pessoa nasceu? '.format(s)))
    s += 1
    a += n
    i = 2024 - n
    if i >= 18:
        ma += 1
    elif i < 18:
        me += 1
print('Ao todo tivemos {}{} menores de idade{},\nE tivemos {}{} maiores de idade{}.'.format(coram, me, corpa, coram, ma, corpa))