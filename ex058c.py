'''Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" um número entre 0 e 10. Só que agora o jogador
  vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep

computador =  randint(0, 10)
print('Olá eu sou o seu computador! \nAcabei de pensar em um número entre 0 e 10! ')
print('Dúvido você Acertar qual é! rsrs')
acertou = False # representa que não acertou
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu chute!? '))
    print('Pausa dramática! ')
    print('-=-' * 15)
    sleep(3)
    palpites += 1
    if jogador == computador:
        acertou = True # Representa que acertou
    else:
        if jogador < computador:
            print('Mais um pouco.... Tente de novo! ')
        elif jogador > computador:
            print('Menos... Tente novamente! ')
print('Acertooou! \nDepois de {} tentativas. PARABENS! ' .format(palpites))

