'''Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50. '''

print('Números PARES entre 1 e 50 são: ')
for cont in range (2, 51, 2):              #Solução ensina no video de resposta que ocupa menos o processador da máquina
    if cont % 2 == 0:
        print(cont, end=' ')
print('FIM')

'''print('Números PARES entre 1 e 50 são: ')
for cont in range (1, 51):                  #Minha primeira solução
    if cont % 2 == 0:
        print(cont, end=' ')
print('FIM')'''

