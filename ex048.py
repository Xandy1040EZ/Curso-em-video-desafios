''' Faça um programa que calcule a soma entre todos os números Ímpares que são múltiplos de 3 e que se encontram no
intervalo de 1 até 500 '''
soma = 0 #Acumador dos multiplos de 3
acum = 0 #Contador dos multiplos de 3
for n in range (1, 501, 2): # esta com 501 pois o ultimo numero é ignorado e p ',2' nos indica que a contagem será pulando de 2 em 2
    if n % 3 == 0:  # Formula para separar os números ímpares múltiplos por 3
        soma += n  #Tambem pode ser escrita dessa forma soma = soma + n
        acum += 1  #Tambem pode ser escrita dessa forma acum = acum + 1
print('São {} Impares entre 1 e 500 e a soma deles é de {} ' .format(acum, soma))