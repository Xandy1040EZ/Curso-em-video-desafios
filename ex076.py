'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequêmcia.
no final mostre uma listagem de preços organizando os dados em forma tabular'''

lista = ('Microondas', 729.00,
         'Máquina de Lavar', 1799.00,
         'Armário', 1180.00,
         'Monitor',  999.00,
         'Copo Térmico', 25.00,
         'Cartucho impressoora', 45.00,
         'Kit de potes', 14.99,
         'Desodorante', 9.90,
         'Caixa de som BoomBox', 1699.00,
         )
print('-' * 40)
print(f'{"LISTA DE COMPRAS":^40}') # ^ centraliza
print('-' * 40)
for produto in range (0, len(lista)):
    if produto % 2 == 0:        #Identificando os itens da listagem par ou seja os produtos
        print(f'{lista[produto]:_<30}' ,end='') #mostra apenas os nomes dos produtos
    else: # identifica os numeros pares
        print(f'R$ {lista[produto]:>7.2f}')
