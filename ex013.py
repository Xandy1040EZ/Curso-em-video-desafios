#Faça um algoritimo que leia o salário de um colaborador e mostre seu novo salário com 15% de aumento

sal = float(input('Digite o salário do colaborador R$ '))
aum = sal + (sal * 0.15)
val = sal * 0.15
print('O Salário atual com 15% de aumento será de R$ {:.2f} '.format(aum))
print('=' * 55)
print('O Salário do colaborador aumentou em R$ {:.2f} '.format(val))
