#Conversor de Base númerica para base binária, octal, hexadecimal

num = int(input('Digite um número inteiro: '))   #Pedindo o número ao usuário
print('1 - Base Binária')
print('2 - Base octal ')                          #Escolhendo as bases
print('3 - Base hexadecimal ')
base = int(input('Escolha entre as opções: 1, 2 ou 3: '))

#Aplicando as Formulas
binário = bin(num) [2:]
octal = oct(num) [2:]
hexadecimal = hex(num) [2:].upper()

# Resultados conforme a escolha do usuário
if base == 1:
    print('Está é a base binária, o número {} em binário é {} ' .format(num, binário ))
elif base == 2:
    print('Está é a base Octal, o número {} em octal é de {} ' .format( num, octal))
elif base == 3:
   print('Está é a base Hexadecimal, o número {} em hexadecimal é de {} '.format(num, hexadecimal))
else:
    print('Você digitou uma opção inválida' ,end='\n' 'Digite uma opção válida 1, 2 ou 3 apenas! ')