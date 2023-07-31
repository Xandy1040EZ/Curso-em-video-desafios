frase = str(input('Digite uma frase: ')).strip()
forma = frase.upper()

print('Processando sua frase . . . ')

print('Quantidades de vezes que a letra "A" aparece na frase é: {} '
      .format(forma.count('A')))

print('Posição da primeira letra "A" na frase é:  {} '
      .format(forma.find('A')+1))

print('Posição em que a letra "A" aparece pela última vez: {} '
      .format(forma.rfind('A')+1))

# Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas Vezes aparece a letra "A"
# - Em qual posição ela aparece pela primeira vez
# - Em qual posição ela aparece pela última vez
