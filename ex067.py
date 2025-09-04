'''Faça um programa que mostre a tabuada de vários números um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o o número solicitador for negativo'''

while True: #laço de loop infinito
    n = int(input('De qual número você que saber a Tabuada? '))
    print('-=' * 20)
    if n < 0: #Testando se o número é negativo, para intterromper o programa
        break
    for c in range (1, 11): #Contador da Tabuada de 0 a 10
        print(f'{n} X {c} = {n*c}') #Formula da tabuada
    print('-=' * 20)
print('-=-=- PROGRAMA FOI ENCERRADO! -=-=-')
