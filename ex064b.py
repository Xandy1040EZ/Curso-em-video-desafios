'''Crie um Programa que leia vários números inteiros pelo teclado. O programa só vai parar quanto o valor digitado
for de 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles'''
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Vocé Digitou {} números e a soma entre eles foi de {}. ' .format(cont, soma))