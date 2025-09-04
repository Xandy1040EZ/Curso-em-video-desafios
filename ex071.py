'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário qual será o valor
a ser sacado (números inteiros) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE: R$ 50, R$ 20, R$ 10 E R$ 1'''

from time import sleep #biblioca de pausa
print('=-' * 22)
print('{:^40}' .format('Seja Bem Vindo ao XBank'))
print('=-' * 22)
print('Notas disponíveis: R$ 50, R$ 20, R$ 10, R$ 1')

while True:  #laço infinito
    valor = int(input('Qual o valor que você deseja sacar!? R$ ')) #colhento o valor
    print('AGUARDE UM MOMENTO!')
    sleep(2) #pausa
    if valor <=0: #verificando se o valor é zero
        print('VALOR INVÁLIDO!\nDIGITE UM VALOR VÁLIDO')
        continue
    #calculo referente a quantidade de cada notas
    nota50 = valor // 50
    valor %= 50

    nota20 = valor // 20
    valor %= 20

    nota10 = valor // 10
    valor %=  10

    nota1 = valor

    print('=-' * 22)
    print('Notas a serem entregues! ')

    # mostrando na tela quantas notas serem entregues de acordo com os valores
    if nota50 > 0:
        print(f'Será entregue {nota50} nota(s) de R$ 50 ')
    if nota20 > 0:
        print(f'Será entregue {nota20} nota(s) de R$ 20')
    if nota10 > 0:
        print(f'Será entregue {nota10} nota(s) de R$ 10')
    if nota1 > 0:
        print(f'Será entregue {nota1} nota(s) de R$ 1')

    print('=-' * 22)
    print('POR GENTILEZA RETIRE \nAS NOTAS NO COMPARTIMENTO INDICADO!' )
    print('=-' * 22)

    #Perguntando se o usuário quer realizar um novo saque
    resp = str(input('Deseja realizar um novo saque? [S/N]')).strip().upper() [0]
    if resp == 'N':
        print('Encerrando....')
        sleep(2)
        print('OBRIGADO POR UTILIZAR NOSSO SERVIÇO!')
        break

