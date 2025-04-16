'''Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" um número entre 0 e 10. Só que agora o jogador
  vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep

tentativas = 1


sorteio = randint(0, 10) #Computador escolhendo um número aleatório entre 0 e 10
jogada = int(input('Escolha um número de 0 a 10! ')) #jogador tentando acertar o número
print('Será que você conseguiu acertar ???? \n  Vamos ver ...  ')
sleep(3) # Pausa de 3 segundos

print ('-=-' * 15)

while jogada != sorteio:
    jogada = int(input('Você errou! Mas você pode tentar novamente! \nEscolha um número de 0 a 10! '))
    print('-=-' * 15)
    sleep(3)
    tentativas += 1
print('VOCÊ ACERTOU!!!')
print ('-=-' * 15)
print('Você precisou de {} tentativas para acertar o número {} ' .format(tentativas, sorteio))
print('-=-' * 15)
