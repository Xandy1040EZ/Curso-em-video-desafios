'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatório. Guarde esses resultados
em um DICIONÁRIO. No final, coleque esse DICIONÁRIO em ordem sabendo que os vencedor tirou o maior número no dado'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'JOGADOR1': randint(1, 6),
        'JOGADOR2': randint(1, 6),
        'JOGADOR3': randint(1, 6),
        'JOGADOR4': randint(1, 6),}

Ranking = list()
print('== VALORES SORTEADOS ==')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORS ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar {v[0]} com {v[1]} pontos no dado.')
    sleep(1)
