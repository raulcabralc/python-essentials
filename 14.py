c = float(input('Qual a temperatura? (Em Celsius) '))
# Float ao inves de int pq o valor e mais preciso e vai precisar de decimais
f = (c*1.8)+32
# Pela ordem nem precisava dos (), mas fds
print('Esta temperatura em Fahrenheit seria {:.1f}F'.format(f))