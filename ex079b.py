'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma LISTA, Caso o número digitado
já exista na lista, ele NÃO SERÁ ADICIONADO no final, serão exibidos todos os VALORES ÚNICOS digitados na lista, em ordem crescente'''

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Voce digitou os valores {números}')
