'''Crie um programa que leia vários números. No final da execução, mostre na tela a Média entre todos os números
e qual foi o menor e o maior valores lidos o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores '''

resp ='S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('QUER CONTINUAR? [S/N] ')).upper().strip() [0]
media = soma / quant
print('Você digitou {} números e a média foi de {} ' .format(quant, media))
print('O Maior valor foi {} e o Menor foi {} ' .format(maior, menor))