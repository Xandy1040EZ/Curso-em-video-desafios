'''Faça um programa que leia um número e mostre o seu fatorial '''

n = int(input('Escolha um número para saber o fatorial: '))   #Colhendo o número
c = n   #contador
f = 1   #Fatorial
print('Fazendo o calculo {}! = ' .format(n) ,end='' )
while c > 0:    #laço enquanto
    print('{} '.format(c) ,end='')  #printando os contadores ex: 5*4*3...
    print('* ' if c > 1 else '= ' ,end='') #definindo o limite para os numeros e o sinal de igual
    f *= c  #Multiplicando os fatores ex: 5*4*3
    c -= 1  #Mostrando o contador com menos 1. pois no fatorial não se multiplica por 0
print('O fatorial de {} é {}. ' .format(n, f))