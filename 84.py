lst = []
lstp = []
lstpes = []

while True:

    lstp.append(str(input('Nome: ')))
    p = int(input('Peso: '))
    lstp.append(p)
    lstpes.append(p)
    lst.append(lstp[:])
    lstp.clear()
    lstpes.sort()

    dnv = str(input('Voce quer continuar? [S/N] ')).strip().upper()
    if dnv in 'N':
        break

print(lst)
print(len(lst))
print(lstpes)
print(lst[:][1])