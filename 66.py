# Nao sei como mas esse exercicio foi apagado entao
# peguei essa resolucao da net que foi bem parecida
# com a minha so pra deixar aqui

print('-=-'*20)
print('Digite alguns valores, para parar digite [999]')
print('-=-'*20)

soma = cont = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} numeros e a soma de todos os números digitados é {soma}')