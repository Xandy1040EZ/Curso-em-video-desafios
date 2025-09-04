'''Crie um Programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagen de números gerados e também indique o menor e o maior valor que estão na tupla'''


from random import randint
num = (randint(1, 100), randint(1, 100), randint(1, 100),randint(1, 100),randint(1, 100))
print('Os valores sorteados foram: ',end='')
for n in num:
    print(f'{n} ',  end='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')