'''Crie um Programa que leia vários números inteiros pelo teclado. O programa só vai parar quanto o valor digitado
for de 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles'''

print('*_*_' * 10)
print('Calcule vários números e pare ao digitar 999!')
acum = 0        #Acumulador quantidade de numeros
n = 0           #Contador de números
soma = 0        #soma entre os números

while n != 999:      #Enquanto n não receber 999 continue
    n = int(input('Digite um número: '))    #Coletando o número
    if n == 999:        #Se o numero informado for 999 parar
        break
    else:               #Senão continue
        acum += 1       #Adicionando mais um número ao contador
        soma += n       #Fazendo a soma entre os números
print('*_*_' * 10)
#Print na tela da quantidade de números e a soma entre eles
print('Você Digitou {} Números ' .format(acum))
print('A SOMA de todos os números é de {} ' .format(soma))
print('*_*_' * 10)