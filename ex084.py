'''Faça um programa que leia NOME E PESO de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais levas'''

# Criando as listas
temp = [] # Lista temporaria para coletar as informações
princ = [] # Lista principal
maior = menor = 0
# Laço de Repetição coletando as informações das listas
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    #Separando os mais leves dos pesados
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear() #limpando a lista temp
    #Validação cada rodada se continua ou não
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
        #resultados
print('-'*45)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ') #len (leitura do tamanho da lista )
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print('-'*45)
