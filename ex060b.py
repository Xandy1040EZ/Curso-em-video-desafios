'''Faça um programa que leia um número e mostre o seu fatorial
com o FOR '''

n = int(input('Escolha um número para saber o fatorial: '))     #Colhendo o número
c = n   #Contador
f = 1   #Fatorial
print('Calculando o fatorial {}! = ' .format(n) ,end='')
for c in range(n, 0, -1):
    f *= c
    if c > 1:
        print('{} * ' .format(c) ,end='')
    else:
        print(' 1 = {} ' .format(f))



