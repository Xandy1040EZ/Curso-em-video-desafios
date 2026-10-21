'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatório. Guarde esses resultados
em um DICIONÁRIO. No final, coleque esse DICIONÁRIO em ordem sabendo que os vencedor tirou o maior número no dado'''
from time import sleep
from random import randint

result = dict()

for jogador in range(1, 5):
     result[f'jogador {jogador}'] = randint(1, 6)
ordenado = sorted(result.items(), key=lambda x: x[1],reverse = True)

print ('-=' * 20)
print('-=-=-JOGANDO OS DADOS-=-=-')
for key, value in ordenado:
    print(f'{key} tirou o número: {value} no dado!')
    sleep(2)
print('-=' * 20)
print(f'O Grande ganhador foi o {ordenado[0][0]} com {ordenado[0][1]} pontos!!!')


