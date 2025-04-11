s = str(input('Escreva seu sexo: [M/F] ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Sexo invalido. Escreva seu sexo com M ou F: ')).upper().strip()[0]
if s == 'M':
    s = 'masculino'
elif s == 'F':
    s = 'feminino'
print('O sexo {} foi registrado.'.format(s))

#if n == 'M':
#    print('Eai macho')
#elif n == 'F':
#    print('Boa tarde donzela')