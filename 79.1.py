lst = []
n = 0
for c in range(0,10):
    m = int(input('Escreva um numero: '))
    lst.append(m)
    if n == m:
        lst.remove(m)
    n = m
print(f'A lista em ordem crescente foi: {lst.sort()}')