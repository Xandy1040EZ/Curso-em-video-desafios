'''Crie um programa que leia vários números. No final da execução, mostre na tela a Média entre todos os números
e qual foi o menor e o maior valores lidos o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores '''

cont = 0                                                           # contador
n = soma = media = 0                                               # variaveis
n = int(input('Digite um Número: '))                               # Coletando o número
soma += n                                                          # Soma recendo a variavel n já com o primeiro número
cont += 1
maior = menor = n                                                  # Identificando maior e menor número
escolha = str(input('QUER CONTINUAR? [ S / N ] ')).strip().upper() # Escolha do usuário se ele deseja continuar ou não

while escolha != 'N':                                               # Enquanto a escolha do usuário for S continua
    n = int(input('Digite um Número: '))
    soma += n                                                       # Soma recendo a variavel n com os novos número
    cont += 1                                                       # Contador recebendo mais um numero na contagem
    # If e Elif fazendo a atualização dos números maior e menor
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    escolha = str(input('QUER CONTINUAR? [ S / N ] ')).strip().upper()  # Escolha do usuário se ele deseja continuar ou não

media = soma / cont                                                     # Calculando a media
# Mostrando na tela os resultados da Quantos números foram digitados, Média, Menor e Maior Número
print(' Você Digitou {} \n A Média deles foi de {} \n O menor número digitado foi {} \n O maior número foi {}. '
                                                                            .format(cont, media, menor, maior))
