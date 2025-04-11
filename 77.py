lst = ('cecis', 'guitarra', 'raul', 'estudar')
v = 'AEIOU'
for l in lst:
    print(f'\nNa palavra {l.upper()} temos: ', end='')
    for letra in l:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')