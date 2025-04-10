'''Desenvolva um programa que leia o primeiro TERMO e a RAZÃO de um PA. No final, mostre os 10 PRIMEIROS NÚMEROS
termos dessa Progressão'''

t = int(input('Informe o PRIMEIRO TERMO da PA: '))
r = int(input('Informe a RAZÃO da PA: '))
#pa = t + (10 * r) formula simplificada
decimo = t + (10 - 1) * r
print('O PRIMEIRO TERMO é de {}, a RAZÃO é de {} '.format(t,r))
for c in range(t, decimo + r, r): #decimo termo + razao
    print(c, end=' ➜ ' )
print('TERMINOU!')

