'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário qual será o valor
a ser sacado (números inteiros) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE: R$ 50, R$ 20, R$ 10 E R$ 1'''

print('=-' * 20)
print('{:^40}'.format('BANCO CEV'))
print('=-' * 20)
valor = int(input('Qual o valor que você deseja sacar: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=-' * 20)
print('Volte sempre ao BANCO CEV! TENHA UM BOM DIA')
