from time import sleep
n = int(input('Me fale um número aí: '))
print('Análisando .... ')
sleep(3) # Faz a pausa na execução do código
if n % 2 == 0: # Conta de divisão por 2 verificando se o resto (%) da divisão é igua a 0
    print('O número {} é PAR '.format(n)) # resposta se for PAR
else:
    print('O número {} é ÍMPAR '.format(n)) # Resposta de for ÍMPAR


#Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou ímpar.
