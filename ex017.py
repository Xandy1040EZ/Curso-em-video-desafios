from math import pow, sqrt

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
soma = pow(co, 2) + pow(ca, 2)
hipo = sqrt(soma)

print('Somando o cateto oposto {:.2f} e o cateto adjacente {:.2f} ao quadrado chegamos \n'
      'ao valor da hipotenusa que é {:.2f} '.format(co, ca, hipo))

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retangulo calcule e mostre o comprimento da hipótenusa
