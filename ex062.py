'''Melhore o DESAFIO 61, pregintanto ao usuário se ele quer mostrar mais termos. O programa encerra quando ele disser
que quer monstrar 0 termos'''

print('GERADOR DE PA')
print('=-' * 10)
primeiro = int(input('Primeiro termo: ')    #Recebendo o primeiro termo
razão = int(input('Informe a Razão: '))     #Recebendo o valor da Razão
termo = primeiro                            #termo
cont =  1                                   #Contador acumulativo
total = 0                                   #Segundo contador acumulativo
mais = 10                                   #contador de termos igual a partir de 10
print('O PRIMEIRO TERMO É {}, E A RAZÃO É DE {}' .format(primeiro, razão))
while mais != 0:                            #Laço de repetição de quando o usuário solicitar mais termos
    total = total + mais                    #Total de termos recebe ele mesmo mais o total de termos a partir de 10
    while cont <= total:                    #Laço de repetição
        print(termo, end=' ➜ ')             #mostrando na tela os termos separados pela seta
        termo += razão                      #termo recebe a razão
        cont += 1                           #contador recebe ele mais um até chegar no decimo termo
    print('Parada Técnica!')
    mais = int(input('Gostaria que fossem mostrados mais quantos termos? '))
print('PA finalizada com {} termos exibidos' .format(total))
