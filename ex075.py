'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares'''

num = (int(input('Digite o 1º valor: ')),
       int(input('Digite o 2º valor: ')),
       int(input('Digite o 3º valor: ')),
       int(input('Digite o 4º valor: ')))

print(f'Você digitou os números: {num}')

print(f'O número 9 aparece {num.count(9)} vezes.') #.count() queonta quantas vezes um valor 09 aparece
#validação valor 3
if 3 in num:
    print(f'O número 3 aparece na posição {num.index(3)+1}') #descobrir em que posição um número está na tupla usei o index.(3)
else:
    print('O Valor 3 não foi digitado, em nenhuma posição')

#numeros pares
print('Os números pares são:', end='')
for pares in num:
    if pares % 2 == 0:  #formula de numeros pares
        print(pares, end=' ')

