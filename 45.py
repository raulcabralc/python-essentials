print(' ---Jogo de PEDRA, PAPEL, TESOURA!---')
print(' ')

import random
pe = 'PEDRA'
pa = 'PAPEL'
te = 'TESOURA'
l = [pe, pa, te]
u = str(input('Escolha entre pedra, papel ou tesoura:\n\n')).upper().strip()
c = random.choice(l)
# EMPATE
if u == pe and c == pe or u == pa and c == pa or u == te and c == te:
    print('\nEMPATE! O computador escolheu {}!\n'.format(u))
# USUARIO ESCOLHEU PEDRA
elif u == pe and c == pa:
    print('\nCOMPUTADOR VENCEU! O computador escolheu PAPEL!\n')
elif u == pe and c == te:
    print('\n\nVOCE VENCEU! O computador escolheu TESOURA!\n')
# USUARIO ESCOLHEU PAPEL
elif u == pa and c == pe:
    print('\nVOCE VENCEU! O computador escolheu PEDRA!\n')
elif u == pa and c == te:
    print('\nCOMPUTADOR VENCEU! O computador escolheu TESOURA!\n')
# USUARIO ESCOLHEU TESOURA
elif u == te and c == pe:
    print('\nCOMPUTADOR VENCEU! O computador escolheu PEDRA!\n')
elif u == te and c == pa:
    print('\nVOCE VENCEU! O computador escolher PAPEL!\n')
else:
    print('\nE necessario escolher apenas entre pedra, papel ou tesoura.\n')