lst = []
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > lst[-1]:
        lst.append(n)
    else:
        c1 = 0
        while c1 < 5:
            if n <= lst[c1]:
                lst.insert(c1, n)
                break
            c1 += 1
print(lst)