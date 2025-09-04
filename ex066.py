'''Crie um programa que leia vários números pelo teclado. O programa só vai parar quando o usuário digitar
 999 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
 (desconsiderando o Flag 999)'''

#adicionando variável Contador e Soma (C/S)
c = s = 0
#Enquanto for Verdade Continua
while True:
    n = int(input('Digite um número: [PARA ENCERRAR 999] '))
    if n == 999: #Quando for digitado 999 parar de receber números
        break #comando de parada
    c += 1
    s += n
print(f'Você Digitou {c} números e a soma deles é de {s}')
