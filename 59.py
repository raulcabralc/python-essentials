from time import sleep
n1 = int(input('Digite um numero: '))
sleep(0.1)
n2 = int(input('Digite outro numero: '))

# Quero colocar tudo isso aqui embaixo dentro de uma variavel, pra colocar
# ela dentro de cada escolha, pra voltar pro painel de escolhas independente
# da escolha e fazer o usuario escolher de novo, ate que ele escolha o 5

#print('-' * 35)

print('-' * 35)
t = 'Escolha uma opcao abaixo para interagir com os dois numeros:\n\033[1;32m[ 1 ]\033[m Somar\n\033[1;32m[ 2 ]\033[m Multiplicar\n\033[1;32m[ 3 ]\033[m Achar o maior\033[1;32m\n[ 4 ]\033[m Novos numeros\033[1;32m\n[ 5 ]\033[m Sair do programa'
print(t)

#print('[ 2 ] Multiplicar')
#print('[ 3 ] Achar o maior')
#print('[ 4 ] Novos numeros')
#print('[ 5 ] Sair do programa')

sleep(0.25)
u = int(input('Escolha: '))
while u != 5:
    if u == 1:
        s = n1 + n2
        sleep(0.25)
        print('A soma entre os dois numeros seria de \033[1;34m{}\033[m.'.format(s))
        sleep(2)
        print('-' * 35)
        print(t)
        sleep(0.25)
        u = int(input('Escolha: '))
    if u == 2:
        m = n1 * n2
        sleep(0.25)
        print('A multiplicacao entre os dois numeros seria de \033[1;34m{}\033[m.'.format(m))
        sleep(2)
        print('-' * 35)
        print(t)
        sleep(0.25)
        u = int(input('Escolha: '))
    if u == 3:
        if n1 > n2:
            ma = n1
        elif n2 > n1:
            ma = n2
        sleep(0.4)
        print('O maior numero entre os dois numeros seria o \033[1;34m{}\033[m.'.format(ma))
        sleep(2)
        print('-' * 35)
        print(t)
        sleep(0.25)
        u = int(input('Escolha: '))
    if u == 4:
        sleep(0.25)
        n1 = int(input('Digite o primeiro numero: '))
        sleep(0.1)
        n2 = int(input('Digite o segundo numero: '))
        sleep(1)
        print('-' * 35)
        print(t)
        sleep(0.25)
        u = int(input('Escolha: '))
print('Saindo do programa...')
sleep(1.5)