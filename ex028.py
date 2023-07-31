from random import randint
from time import sleep
sort = (randint(0, 5)) # Fez o computador escolher um número 0 e 5
num = int(input('Tente acertar o número que estou pensando entre 0 e 5: '))
print('Será que você Acertou ? ..... ')
sleep(3) # Faz uma pausa na execução do código
print ('-=-' * 20)
if sort == num:
    print('Parabéns Você Ganhou !!!!!!!') # Resultado caso o usuário acerte
else:
    print('Você perdeu :\ \n \nTente novamente \n ')
print('Número escolhido pela máquina foi o {} e o seu foi o {}'.format(sort, num))
print('-=-' * 20)

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
