'''Crie um programa onde o usuário  possa digitar SETE VALORES NÚMERICOS e cadastre-os em uma LISTA ÚNICA que mantenha separados os valores PARES
e  ÍMPARES. No final mostre os valores pares e ímpares em ordem CRESCENTE
'''

num = [[], []] # criando as listas: geral; pares; e impares (pares [0] e impares [1])
valor = 0
for c in range(1, 8): # repetição por 7x a coleta dos valores
    valor = int(input(f'Digite {c}° valor: '))
    #Verificação se é par ou impar
    if valor % 2 == 0:
        num[0].append(valor) # 0 representa o par na lista, assim já direciona para a lista correspondente
    else:
        num[1].append(valor) # 1 representa o impar na lista, assim já direciona para a lista correspondente
print('-=' * 30)
#Colando as listas em ordem crescente
num[0].sort()
num[1].sort()
#mostrando os resultados
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores pares digitados foram: {num[1]}')
