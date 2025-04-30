'''Escreve um Programa que leia un número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
SEQUÊNCIA DE FIBONNACCI
Ex. 0 > 1 > 1 > 2 > 3 > 5 > 8 '''

print('=-=-=-=-=-= Vamos gerar uma sequência de FIBONNACCI =-=-=-=-=-=')
n = int(input('Informe quantos termos: '))      #Coletando os termos
print('*-*-' * 20)

t1 = 0      # A Sequencia sempre comeca com o 0
t2 = 1      # Depois do 0 sempre o segundo termo será o 1
cont = 3    # Nesse caso o contador começa no 3 pois os dois primeiros termos já estão definidos

print('*-*-' * 20)
print('{} → {} →'.format(t1, t2) ,end= '') #Print da estrutura

while cont <= n:        #Enquando o contador não chegar no numero informado continuamos
    t3 = t1 + t2        #Formula da sequencia
    cont += 1       #Somando ao contador
    t1 = t2         #Passando o valor do t2 original para o t1
    t2 = t3         #Passando o valor do t3 original para o t2
    print(' {} → '.format(t3), end='') #Print recebendo a instrutura continua

print('TERMINAMOS')
print('*-*-' * 20)




