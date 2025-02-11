'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria de acordo com a idade '''
import datetime
atual = datetime.date.today().year
nasc = int(input('Informe o ano de nascimeto do atleta: '))
idade = atual - nasc

if idade <= 9:
    print('SUA CATEGORIA É: MIRIM')
elif idade <= 14:
    print('SUA CATEGORIA É: INFANTIL')
elif idade <= 19:
    print('SUA CATEGORIA É: JUNIOR')
elif idade <= 25:
    print('SUA CATEGORIA É: SÊNIOR')
else:
    print('SUA CATEGORIA É: MASTER')


