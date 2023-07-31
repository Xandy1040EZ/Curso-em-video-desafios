n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segungo número: '))
n3 = int(input('Digite o terceiro número: '))
print('Os números digitados foram {}, {} e o {} '.format(n1, n2, n3))
# Encontrando o número Maior
maior = n1
if n1 > n2:
    maior = n2
if n3 > maior:
    maior = n3
# Encontrando o número menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor foi o de  {} '.format(menor))
print('O maior valor foi o de {} '.format(maior))
# Faça um programa que leia três números e mostre qual é o Maior e o menor

