'''Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" um número entre 0 e 10. Só que agora o jogador
  vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep

tentativas = 2


sorteio = (randint(0, 10)) #Computador escolhendo um número aleatório entre 0 e 10
jogada = int(input('Escolha um número de 0 a 10! ')) #jogador tentando acertar o número
print('Será que você conseguiu acertar ???? \n  Vamos ver ...  ')
sleep(3) # Pausa de 3 segundos

print ('-=-' * 12)

while jogada != sorteio:
    jogada = int(input('VOCÊ ERROU! \nVOCÊ GANHOU MAIS UMA TENTATIVA! '))
    print('-=-' * 12)
    sleep(3)
    if jogada == sorteio:
        print('-=-' * 12)
        print('PARABÉNS VOCÊ ACERTOU!!! ')
    elif jogada != sorteio:
        tentativas += 1
else:
    print('-=-' * 12)
    print('VOCê PRECISOU DE {} TENTATIVAS, PARA ACERTAR O NÚMERO {} ' . format(tentativas, sorteio))



