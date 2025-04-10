'''Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lido '''

#Contador do maior e menor
maior = 0
menor = 0
for pessoa in range(1, 6): #laço de repetição 5x
    peso = float(input('Qual é o Peso da {}° pessoa? ' .format(pessoa)))  #coletando o peso de 5 pessoas
    if pessoa == 1:
        maior = peso #maior peso
        menor = peso #menor Peso
    else:
        # Se o maior peso lido for de maior do eu tenho ele ocupara a vaga de maior peso
       if peso > maior:
            maior = peso
        # Se o menor peso lido for de menor do eu tenho ele ocupara a vaga de menor peso
       if peso < menor:
            menor = peso
#print mostrando o maior e o menor peso no resultado
print('A Pessoa mais pesada têm {}Kg \nA Pessoa Menos Pesada têm {}Kg '.format(maior, menor))

