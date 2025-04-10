'''Desenvolva um programa que leia 6 números e mostre a soma APENAS daqueles que forem PARES.
OBS: SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERAR'''
soma = 0        #Soma dos números
par = 0         #Acumulador dos números pares
for n in range(1, 7):       # Fazer o print 6x
    num = int(input('Digite o {} valor : ' .format(n)))     # o format para mostrar qual é a posição do valor 123...
    if num % 2 == 0:    #Formula para identificar números pares
        soma += num     # Soma dos números PARES, pois esta dentro od if
        par += 1        # Contagem dos números PARES, pois está dentro do if
print('Foram Digitados {} PARES, a SOMA deles é de {}  ' .format(par, soma))

#ATENÇÃO COM A IDENTAÇÃO O IF ESTÁ DENTRO DO LAÇO DE REPETIÇÃO, SE ESTIVER FORA NAO FUNCIONARA


