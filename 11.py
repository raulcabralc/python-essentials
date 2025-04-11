l = int(input('Qual a largura da parede? (em metros) '))
a = int(input('Qual a altura da parede? (em metros) '))
area = l*a
t = area/2
print('A area dessa parede seria de {}m², seriam necessarios {:.0f}L de tinta para pinta-la inteira.'.format(area, t))