'''Crie um programa que crie uma MATRIZ de dimesão 3x3 e preencha com valores lidos pelo teclado:
No final mostre a MATRIZ na tela com a formatação correta.'''

#criando a lista com 3 listas dentro
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#laço de repetição
for l in range(0, 3): #laço das linhas (l)
    for c in range(0, 3):#laço das colunas (c)
        matriz [l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3): #laço das linhas (l)
    for c in range(0, 3): #laço das colunas (c)
        print(f'[{matriz[l][c]:^5}]', end='') #print da matriz centralizada
    print()
