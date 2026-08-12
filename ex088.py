'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar QUANTOS JOGOS serão gerados
e vai sortear 6 números entre 01 e 60 para cada jogo. cadastrando tudo em uma lista composta'''
from random import randint
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 3, f'<   BOA SORTE!!!   >', '-=' * 3)
