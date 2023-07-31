from math import sin, cos, radians, tan

ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('O Seno referente ao ângulo vale {:.2f}, \no Cosseno referente ao ângulo vale {:.2f} '.format(seno, cos))
print('A tangênte refernte ao ângulo vale {:.2f} '.format(tang))

#Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
#e tangente desse ângulo
