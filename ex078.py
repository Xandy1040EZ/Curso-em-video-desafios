'''Faça um proograma que leia 5 VALORES NÚMEROS e guarde-os em uma lista.
No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas posições na lista'''


lista = [] # Lista criada
maior = 0 # maior
menor = 0 #menor
#Coletando os 5 valores da lista
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a lista na Posição {c}: ')))
    #Identificando o maior e o menor
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=- ' * 20)
print(f'Você Digitou os seguintes números para a lista: {lista}')
#Selecionando o maior valor
print(f'O Maior número da lista foi o {maior}, na(s) Posição(ões) ', end=' ')
for ind, valor in enumerate(lista):
    if valor == maior:
        print(f'{ind}... ', end= '')
print()
#Selecionando o menor Valor
print(f'O Menor número da lista foi o {menor}, na(s) Posição(ôes) ', end= '')
for ind, valor in enumerate(lista):
    if valor == menor:
        print(f'{ind}... ', end= '')

