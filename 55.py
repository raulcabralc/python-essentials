ma = 0
me = 0
for c in range(1, 6):
    n = float(input('Qual o peso em kg da {} pessoa? '.format(c)))
    if c == 1:
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
print('O maior peso foi de\033[1;33m {} \033[mkg.'.format(ma))
print('O menor peso foi de\033[1;33m {} \033[mkg.'.format(me))