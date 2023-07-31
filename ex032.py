from time import sleep
from datetime import date

ano = int(input('Qual ano quer analisar? Digite 0 para analisar o ano atual: '))  # pedindo ao usuario um ano
print('Análisando se {} é ano bissexto: '.format(ano))
sleep(3)
if ano == 0:
    ano = date.today().year # Selecionando o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # Formula do ano bissexto se ano é divisivel por 4,
    # ou se o ano for terminado em 00 se é divisivel por 400
    print('O ano {} é BISSEXTO '.format(ano)) # se for BISSEXTO
else:
    print('O ano {} NÃO é BISSEXTO '.format(ano)) # Senão for BISSEXTO


'''Faça um programa que leia um ano qualquer e msotre se ele é bissexto'''
