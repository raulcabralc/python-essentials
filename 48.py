s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
print('A soma de todos estes numeros e: {}'.format(s))