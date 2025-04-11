print('-'* 60)
print(' ' * 17, 'DETECTOR DE PALINDROMOS')
print('-'* 60)
n = str(input('Escreva algo: ')).upper().strip()
pa = n.split()
j= ''.join(pa)
i = ''
for c in range(len(j) -1, -1, -1):
    i += j[c]
print('Voce digitou a frase \033[1;34m{}\033[m.'.format(n))
print('O inverso dessa frase seria \033[1;34m{}\033[m.\n'.format(i))
if j == i:
    print('A frase \033[1;33m{}\033[m e um palindromo.'.format(n))
else:
    print('A frase \033[1;33m{}\033[m nao e um palindromo.'.format(n))

#if n == i:
#    print(n, i)
#else:
#    print('cu')