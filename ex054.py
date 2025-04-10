'''Crei um programa que leia o ano de nascimento de 7 pessoas e no final mostre se quantas pessoas ainda não atigiram a
maior idade e quantas já são maiores'''

from datetime import datetime #Biblioteca de tempo dia mes e ano

ano = datetime.now().year #para usar o ano atual (2025)
#Contador de quantas pessoas são de maior ou menor
maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}° Pessoa: ' .format(c))) #colhendo em que ano a pessoa nasceu
    idade = ano - nasc #conta para decobrir a idade
    if idade <= 21: #Apartir de 21 anos a pessoa está na maioridade
        maior += 1 #Contador para a pessoa menor de idade (no caso +1)
    else:
        menor += 1 #Contador para a pessoa maior de idade (no caso + 1)
# Print para mostrar a quantidade de pessoas que estão na maioridade e que ainda não estão
print('São {} MENORES DE 21 Anos, ainda não estão na Maioridade! '
      '\n{} Pessoas MAIORES DE 21  ANOS, chegaram na MAIORIDADE!' .format(menor, maior))
