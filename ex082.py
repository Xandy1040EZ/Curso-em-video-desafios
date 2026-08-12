'''Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma lista
Depois dissi, crie DUAS LISTAS EXTRAS que vão conter apenas os valores PARES e os valores IMPARES digitados, respectivamente.
No final mostre o conteúdo das três listas geradas'''

#criando as listas
lista = []
impares = []
pares = []

#Coletando os números
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    print('Número digitado foi adicionado na lista.')

#Verificando os números se são impares ou pares
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    #Validando continuação
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('Resposta inválida! Digite apenas S ou N!')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        print('Obrigado por utilizar o programa!')
        break


#Resultados
print('-=' * 30)
print(f'Os números digitados foram: {lista}' )
print(f'Esses são os números pares: {pares}')
print(f'Esses são os números impares {impares}')

