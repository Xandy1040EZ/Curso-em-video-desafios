'''Faça um programa que leia um número inteiro e diga se ele é ou não um número PRIMO'''

num = int(input('Digite um número: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m' ,end='')
        div += 1
    else:
        print('\033[31m' ,end='')
    print('{} '.format(c), end='')
print('\n\033[mO Número {} foi divisível {} vezes ' .format(num, div))
if div == 2:
    print('E por ele ser divisível por 1 e por ele mesmo o número {} é PRIMO! ' .format(num))
else:
    print('E por ele não ser divisível SOMENTE entre 1 e por ele mesmo o {} não é PRIMO ' .format(num))