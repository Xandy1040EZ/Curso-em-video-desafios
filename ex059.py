'''Crie um programa que leia ois valores e mostre um menu na tela.'''
from time import sleep
#Coletando os números
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

menu = 0 #guardando as opções escolhidas

#Criando o Menu com o metodo de repetição while (enquanto) o loop ficará até o usuário escolher a opção 5 de SAIR
while menu != 5:
    print('-=-=-=-=-=-=-= MENU =-=-=-=-=-=-=-')
    print('''        [1] SOMAR
        [2] MULTIPLICAR
        [3] Qual O MAIOR NÚMERO
        [4] NOVOS NÚMEROS
        [5] SAIR''')
    menu = int(input(' >>>>>> ESCOLHA UMA DAS OPÇÕES ACIMA: ' )) #Coletando a escolha do usuário
    if menu == 1: #escolha 1
        print('Você escolheu a opção 1 - SOMAR ')
        print('A soma entre {} + {} = {} ' .format(n1, n2, n1 + n2))
    elif menu == 2: #escolha 2
        print('Você escolheu a opção 2 - MULTIPLICAR ')
        print('A multiplicação entre {} * {} = {} ' .format(n1, n2, n1 * n2))
    elif menu == 3: #escolha 3
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Você escolheu a opcão 3 - Qual O MAIOR NÚMERO')
        print('O número maior entre {} e {} é o {:.0f} ' .format(n1, n2, maior))
    elif menu == 4: #escolha 4
        print('Você escolheu a opção 4 - NOVOS NÚMEROS ')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif menu == 5: #escolha 5
        print('Você escolheu a opção 5 - SAIR:')
        print('Obrigado! por utilizar a aplicação! ')
    else:
        print('Opção inválida, Tente novamente!')
    sleep(2)




