#Identifique se o número é maior (>) ou menor(<) ou se são iguais
#Colhetando os números

print('Digite dois números a seguir para descobrir qual é o > e o < entre eles: ' , end='\n' )
num1 = int(input('Digite o primeiro número inteiro:'))
num2 = int(input('Digite o segundo número inteiro: '))

#Comparando os números

if num1 > num2:
    print('O número {} é MAIOR que o número {} ' .format(num1, num2))
    print('O número {} é MENOR que o número {} '.format(num2, num1))
elif num1 < num2:
    print('O  Número {} é MAIOR que o número {} ' .format(num2, num1))
    print('O número {} é MENOR que o número {} '.format(num1, num2))
else:
    print('OS NÚMEROS SÃO IGUAIS!!! ')