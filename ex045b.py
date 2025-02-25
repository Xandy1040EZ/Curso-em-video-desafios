from random import randint
from time import sleep


escolha = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
pc = randint(1, 3)
emojis = {1: '🪨', 2: '📄', 3: '✂️'}
print('Escolha uma das opções para começar o JOKENPÔ: ')
print('[1] {emojis[1]} Pedra\n[2] {emojis[2]} Papel\n[3] {emojis[3]} Tesoura' .format(emojis=emojis))
while True:
    try:
        jog = int(input('Qual sua Jogada: '))
        if jog not in escolha:
            print("Jogada inválida! Por favor, escolha 1, 2 ou 3.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Por favor, insira um número entre 1 e 3.")


print('\33[1;31m JO \33[m ') #Cor Vermelha
sleep(1)
print('\33[1;33m KEN \33[m') #Cor Amarela
sleep(1)
print('\33[1;32m PÔ! \33[m') #Cor Verde
sleep(1)
print('-=-' * 17)
print('Você Jogou: {} {}' .format(escolha[jog],emojis[jog]))
print('-=-' * 17)
sleep(1)
print('O PC escolheu: {} {}' .format(escolha[pc],emojis[pc]))
print('-=-' * 17)
sleep(1)
#Sorteando as opções para mostra quem venceu
if pc == 1: #PC Jogou Pedra
    if jog == 1:
        print('\33[1;40;47m EMPATE \33[m 🤝🤝 ') #Cor Branca e fundo cinza
    elif jog == 2:
        print('\33[1;36;40m JOGADOR VENCE \33[m 🏆🏆')
    elif jog == 3:
        print('\33[1;41;43m PC VENCE \33[m 😞😞')
    else:
        print('-=-' * 17)
        print('JOGADA INVÁLIDA! 🚫🚫')
        print('-=-' * 17)
if pc == 2: #PC Jogou Papel
    if jog == 1:
        print('\33[1;41;43m PC VENCE \33[m 😞😞 ')
    elif jog == 2:
        print('\33[1;40;47m EMPATE \033[m 🤝🤝 ') #Cor Branca e fundo cinza
    elif jog == 3:
        print('\33[1;36;40m JOGADOR VENCE \33[m 🏆🏆')
    else:
        print('-=-' * 17)
        print('JOGADA INVÁLIDA! 🚫🚫 ')
        print('-=-' * 17)
if pc == 3: #PC Jogou tesoura
        if jog == 1:
            print('\33[1;36;40m JOGADOR VENCE \33[m 🏆🏆' )
        elif jog == 2:
            print('\33[1;41;43m PC VENCE \33[m 😞😞 ')
        elif jog == 3:
            print('\33[1;40;47m EMPATE \33[m 🤝🤝 ') #Cor Branca e fundo cinza
        else:
            print('-=-' * 17)
            print('JOGADA INVÁLIDA! 🚫🚫')
            print('-=-' * 17)