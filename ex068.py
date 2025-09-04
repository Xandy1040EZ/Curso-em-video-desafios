'''Faça um programa que joge PAR ou ÍMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitorias consecutivas qu ele conquistou no final do jogo'''
#Importando a biblioteca random valores aleatorios
from random import randint
v = 0 #Acumulativo de vitorias
while True:
    #Validação de joga P ou I
    while True:
        jog = str(input('Escolha PAR ou ÍMPAR!? [P / I]')).upper().strip() [0]
        if jog in ('P', 'I'):
            break
        print('Jogada Inválida tente novamente!')
        #Colhendo as informações
    n_jog = int(input('Agora escolha um número: '))
    n_comp = randint(1,10) #sorteando um numero de 0 a 10
    total = n_jog + n_comp #soma dos numeros

    print(f'Você jogou {n_jog} e seu computador jogou {n_comp} ')
    print(f'O Resultado foi {total} PAR! ' if total % 2 == 0 else f'O Resultado foi {total} ÍMPAR!') #identificando se é par ou impar pela formula

    if jog == 'P' and total % 2 == 0 or jog == 'I' and total % 2 != 0: #caso o jogador escolha a opção certa par ou impar
        v += 1 #a cada vitoria soma-se mais uma
        print('VOCÊ VENCEU!!!')
    else:
        print('VOCÊ PERDEU!!!')
        break
print(f'Você ganhou {v} vezes seguidas! ') #mostrando quantas vezes o jogador ganhou seguidas