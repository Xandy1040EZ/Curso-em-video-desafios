print('Será que forma um triângulo??? ')
print('-=-' * 12)
a = float(input('Qual é o valor da primeira reta? '))
b = float(input('Qual é o valor da segunda reta? '))
c = float(input('Qual é o valor da terceira reta? '))
print('-=-' * 12)
#Formula da condicional do triângulo,
#(A soma das duas retas têm que ser maior que a terceira sempre.)
if a + b > c and a + c > b and b + c > a:
    print('\033[1;32mO Triângulo será formado! \033[m ')
else:
    print('\033[1;31mO Triângulo não será formado! \033[m')

'''Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo'''