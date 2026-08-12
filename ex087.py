'''Aprimore o desafio anterior, mostre no final:
A) A SOMA de todos os valores pares;
B) A SOMA de dos valores da terceira coluna;
c) O maior valor da segunda linha.'''

#criando a lista com 3 listas dentro
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior =scoluna = 0
#laço de repetição
for l in range(0, 3): #laço das linhas (l)
    for c in range(0, 3):#laço das colunas (c)
        matriz [l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3): #laço das linhas (l)
    for c in range(0, 3): #laço das colunas (c)
        print(f'[{matriz[l][c]:^5}]', end='') #print da matriz centralizada
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores, pares é {spar}')
for l in range(0, 3):
    scoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scoluna}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1] [c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')




