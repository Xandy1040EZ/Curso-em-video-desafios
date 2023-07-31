nome = str(input('Digite o nome de alguma cidade: ')).strip()
print('Análisando o nome . . .')
form = nome.capitalize() # Formanto para que só a letra inicial fique em Maiúsculas para a análise
print('O nome da cidade começa por -- "Santo" -- ? {} '.format('Santo' in form))

# Faça um programa que leia o nome de um ciade e diga se ela começa ou não com o nome "Santo"