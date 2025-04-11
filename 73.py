print('\nBRASILEIRAO SERIE A\n')
tpl = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Bahia', 'Sao Paulo', 'Cruzeiro', 'Galo', 'Atletico Paranaense', 'Vasco')
a = tpl[0:6]
b = tpl[-4:]
c = sorted(tpl)
d = tpl.index('Botafogo') + 1
print('{}-{}-{}'.format('\033[1;33m', '\033[1;34m', '\033[m')*50)
print('Lista dos primeiros 5 colocados: {}'.format(a))
print('{}-{}-{}'.format('\033[1;33m', '\033[1;34m', '\033[m')*50)
print('Lista dos ultimos 4 colocados: {}'.format(b))
print('{}-{}-{}'.format('\033[1;33m', '\033[1;34m', '\033[m')*50)
print('Lista em ordem alfabetica: {}'.format(c))
print('{}-{}-{}'.format('\033[1;33m', '\033[1;34m', '\033[m')*50)
print('O Botafogo esta na {} posicao.'.format(d))
print('{}-{}-{}'.format('\033[1;33m', '\033[1;34m', '\033[m')*50)