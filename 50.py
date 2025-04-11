from time import sleep
s = 0
cc = 0
print('A seguir voce escolhera numeros, os pares serao somados e os impares serao desconsiderados.')
sleep(2.5)
for c1 in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
        cc += 1
        #if cc == 1:
            #print('O somatorio do unico numero par acima seria de {}'.format(s))
        #else:
            #print('O somatorio dos {} numeros acima seria de {}.'.format(cc, s))
print('O somatorio do(s) {} numero(s) par(es) acima seria de {}.'.format(cc, s))