'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de ZERO até VINTE
Seru progrma deverá ler um número pelo teclado entre 0 e 20 e mostra-lo por extenso'''

# Criando a Tupla com os números por extenso
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True: #Laço de repetição
    num = int(input('Digite um número entre 0 e 20, para vê-lo  por extenso: ')) #pedindo número ao usuario
    #Verificando se esta dentro do intervalo de 0 a 20
    if 0 <= num <= 20:
        print(f'VOCÊ DIGITOU {num}, ele por extenso é {extenso[num].upper()}') #extenso[num - 1] seleciona a tupla com os números; upper() letras maiusculas
        break
    else:
        print('Valor Inválido! Digite novamente')