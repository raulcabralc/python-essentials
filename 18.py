import math
a = int(input('Digite um angulo em graus: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O seno deste angulo seria {:.2f}\nO cosseno deste angulo seria {:.2f}\nA tangente deste angulo seria {:.2f}.'.format(sen, cos, tan))