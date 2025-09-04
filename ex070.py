'''Crie um Programa que leia o NOME e o PREÇO de vários produtos. o pragrama deverá perguntar se o USUÁRIO
vai continuar e no final mostre
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000,00
C) Qual é o NOME do produto mais BARATO'''
#Variaveis
gasto = mil = barato = cont = 0
produto_barato = '' #salva nome do produto
while True: #laço infinito
    #colhendo as info
    produto = str(input('Informe qual é o produto: '))
    preco = float(input('Qual o preço? R$ '))
    cont += 1
    gasto += preco #somando os valores
    # Validando preco maior que R$ 1000
    if preco >= 1000:
        mil += 1
    # Validando produto mais Barato
    if cont == 1 or preco < barato:
        barato = preco
        produto_barato = produto #nome do produto
    #Continua ou não
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar outro produto [S/N]')).strip().upper() [0]
    if continuar == 'N':
        break

#estatisticas
print(f'O valor da compra total foi de R$ {gasto:.2f}')
print(f'Foram {mil} produtos acima dos R$ 1.000,00 ')
print(f'O produto mais barato foi o {produto_barato}, custando R$ {barato:.2f}')





