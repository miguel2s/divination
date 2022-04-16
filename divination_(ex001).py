'''import random
sorn = str(input('Vou pensar em um número de 0 a 5, será que você consegue adivinhar qual número eu estou pensando? (S/N) ')).lower()
bot = random.randint(0, 5)
if sorn == 's':
    n = int(input('Vamos ver se você é bom mesmo, qual número eu estou pensando? '))
    if n == bot:
        print('PARABÉNS!!! Realmente você acertou! :D')
    else:
        print('NÃO FOI DESSA VEZ!')
else:
    l = int(input('Que isso, vamos tentar, não custa nada, fale-me um número de 0 a 5 '))
    if l == bot:
        print('VOCÊ ACERTOU!!! Viu só, você foi muito bem, parabéns! :)')
    else:
        print('Você tinha razão, não consegue mesmo não! kkkkkk...XD')'''

from random import randint
from time import sleep
comp = randint(0,5) # Faz o computador "pensar" em um número
print('-=-'*19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-'*19)
player = int(input('Em que número eu pensei? '))  # Jogador tenta advinhar o número
print('PROCESSANDO....')
sleep(2)
if player == comp:
    print('PARABÉNS! Você conseguiu me vencer, eu pensei justamente no {}!'.format(comp))
else:
    print('Pensei no número {} e não no número {}'.format(comp, player))