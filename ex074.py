'''Crie um Programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagen de números gerados e também indique o menor e o maior valor que estão na tupla'''

import random
#Gerendo números aleatorio nas tuplas
#random,randint faz o sorteio entre os números 1 e 100
num = tuple(random.randint(1,100)
       for c in range (5)) #usando o for para escolher 5 numeros

print('=-=' * 18)
print(f'Os números sorteados são: ', end='')
print('=-=' * 18)
print("Maior número:", max(num))
print('=-=' * 18)
print("Menor número:", min(num))
print('=-=' * 18)