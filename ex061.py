'''Refaça o Desafio 51. lendo o primeiro termo e a Razão de uma PA, monstrando os 10 primeiros termos da progressão
usando a estrutura - WHILE'''

t = int(input('Informe o PRIMEIRO TERMO da PA: ')) #Recebendo o primeiro termo
r = int(input('Informe a RAZÃO da PA: ')) #Recebendo o valor da Razão
cont = 0 #Contador
termo = t #termo
print('O PRIMEIRO TERMO É {}, E A RAZÃO É DE {}' .format(t, r))
while cont < 10: #ENQUANTO O CONTADOR FOR MENOR DO QUE 10 CONTINUA
    print(termo, end=' ➜ ') #mostrando na tela os termos separados pela seta
    termo += r #termo recebe a razão
    cont += 1 #contador recebe ele mais um até chegar no decimo termo
print('ACABAMOS!!!')
