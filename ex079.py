'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma LISTA, Caso o número digitado
já exista na lista, ele NÃO SERÁ ADICIONADO no final, serão exibidos todos os VALORES ÚNICOS digitados na lista, em ordem crescente'''

lista = [] #criando a lista

while True: #laço de repetição
    num = int(input('Digite um número para a lista: ')) #colentado os números

    if num not in lista: #validação de números iguais
        lista.append(num) #adicionando os números na lista
        print('Número adicionado com sucesso')
    else:
        print('Número duplicado - não será incluído')
        # Confirmação se o usuário quer continuar
    resp = input('Deseja continuar? [S/N]').strip().upper()
    # Validando a resp. se é  S ou N apenas
    while resp not in 'SN':
        print('Resposta ínválida, Para continuar digite apenas S ou N')
        resp = input('Deseja continuar? [S/N] ').strip().upper()

    if resp == 'N': #Se o N for escolhido saimos do laço de repetição
        break
#Mostrando o resultado
print('-=' * 26)
print(f'Os números digitados para a lista foram: {lista} ') #Mostrando a lista na ordem em que foi digitada

lista.sort() #O método .SORT() para organizar os numeros em ordem crescente
print(f'Os números da lista em ordem crescente: {lista}') # Mostrando os número em ordem


