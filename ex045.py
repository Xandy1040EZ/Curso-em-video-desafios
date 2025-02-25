'''Crie um programa que faça o computador jogar jokenpô (Pedra, Papel ou Tesoura'''
from random import randint
from time import sleep

escolha ={1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
pc = randint(1, 3)
print('Escolha uma das opções para começar o JOKENPÔ: ')
print('''[ 1 ] Pedra 
[ 2 ] Papel
[ 3 ] Tesoura''')
jog = int(input('Qual sua Jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-=-' * 17)
print('Você Jogou: {} ' .format(escolha[jog]))
print('-=-' * 17)
print('O PC escolheu: {} ' .format(escolha[pc]))
print('-=-' * 17)
#Sorteando as opções para mostra quem venceu
if pc == 1: #PC Jogou Pedra
    if jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE')
    elif jog == 3:
        print('PC VENCE')
    else:
        print('JOGADA INVÁLIDA!')
if pc == 2: #PC Jogou Papel
    if jog == 1:
        print('PC VENCE')
    elif jog == 2:
        print('EMPATE')
    elif jog == 3:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

if pc == 3: #PC Jogou tesoura
        if jog == 1:
            print('JOGADOR VENCE')
        elif jog == 2:
            print('PC VENCE')
        elif jog == 3:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')










