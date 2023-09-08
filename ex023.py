num = int(input('Digite um número de 0 à 9999: '))
print('ANALISANDO O NÚMERO {} ...'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidades: {} '.format(u))
print('Dezenas: {} '.format(d))
print('Centenas: {} '.format(c))
print('Milhar: {} '.format(m))





"""Faça um programa que leia um número de 0 a 9999 e mostre na tela 
cada um dos digítos separados"""