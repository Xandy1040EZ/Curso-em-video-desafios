'''Desenvolva uma lógica que leia o peso do usuário e a altura de uma pessoa calcule o IMC e a classifique'''

#Coletando informações do usuário
peso = float(input('Nos infome qual é o seu peso atual: '))
altura = float(input('Agora nos infome qual é a sua altura: '))

print('Seu Peso é de {:.2f} Kg ' .format(peso))
print('Sua altura é de {:.2f} m ' .format(altura))

#Calculando o Imc
imc = peso / (altura ** 2 )

#Classificações
if imc < 18.5:
    print('Sua classificação foi de {:.2f}: ABAIXO DO PESO IDEAL ' .format(imc))
elif 18.5 <= imc <= 24.9:
    print('Sua Classificação foi de {:.2f}: PESO IDEAL ' .format(imc))
elif 25 <= imc <= 29.9:
    print('Sua Classificação foi de {:.2f}: SOBREPESO ' .format(imc))
elif 30 <= imc <= 34.9:
    print('Sua Classificação foi de {:2.f}: OBESIDADE GRAU I ' .format(imc))
elif 35 <= imc <= 39.9:
    print('Sua Classificação foi de {:.2f}: OBESIDADE GRAU II ' .format(imc))
elif imc >= 40:
    print('Sua Clasificação foi de {:.2f}: OBESIDADE GRAU III ' .format(imc))