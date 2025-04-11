print('{}-{}-'.format('\033[1;34m', '\033[1;33m') * 25)
print(' ' * 13, 'Sucessao de Fibonacci')
print('{}-{}-'.format('\033[1;34m', '\033[1;33m') * 25)

print('{}~{}'.format('\033[1;34m', '\033[m') * 50)

f = int(input('Quantos termos voce quer mostrar? '))

t1 = 0
t2 = 1

print('{} ➝  {}'.format(t1, t2), end='')

c = 3
while c <= f:
    t3 = t1 + t2
    print(' ➝  {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

#while p <= 10:
#    fb = (f - 1) + (f - 2)
#    print(' {}'.format(fb), end=' ➝ ')
#    p += 1