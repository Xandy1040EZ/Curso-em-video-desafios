'''Crie um programa que leia VÁRIOS NÚMEROS e colocar em uma lista. Depois disso mostre:
A) QUANTOS números foram digitados;
B) A lista de valores, ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista'''

lista = [] #Criando a Lista

#Laço de repetição infinito
while True:
    n = int(input('Digite um número para ser adicionado na lista: ')) #Coletando os numeros
    lista.append(n) #Adicionando a lista
    print('Número adicionado com sucesso! ')

    #Perguntando se o usuário deseja continuar
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    #Laço de repetição resposta S/N
    while resp not in 'SN':
        print('Resposta inválida! Digite apenas S ou N!')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('Obrigado por utilizar o programa! \nVeja o resultado a seguir!')
        break

# Resultados
print('-=' * 30)
print(f'Na lista tem, {len(lista)} números adicionados.')
lista.sort(reverse=True)
print(f'Lista de números em ordem descrescente {lista} ')
if 5 in lista:
    print('O Número 5 foi adicionado na lista!')
else:
    print('O Número 5 não foi adicionado na lista!')
print('-=' * 30)
