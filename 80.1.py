lst = []
for c in range(0,5):
    n = int(input('Digite um numero: '))
    if len(lst) == 0:
        lst.insert(0, n)
    else:
        if n < min(lst):
            lst.insert(0, n)
        elif n > max(lst):
            lst.insert(len(lst), n)
        else:
            lst.insert(3, n)
print(lst)