'''Crie um programa que crie uma MATRIZ de dimesão 3x3 e preencha com valores lidos pelo teclado:
No final mostre a MATRIZ na tela com a formatação correta.'''

matriz = [[], [], []] #Declarando a lista e dentro mais 3 listas
valor = 0
#laços de repetição
for c in range(1, 4):
    valor = int(input(f'Digite {c}° valor da matriz: '))
    matriz[0].append(valor)
for c in range(4, 7):
    valor = int(input(f'Digite {c}° valor da matriz: '))
    matriz[1].append(valor)
for c in range(7, 10):
    valor = int(input(f'Digite {c}° valor da matriz: '))
    matriz[2].append(valor)

print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
