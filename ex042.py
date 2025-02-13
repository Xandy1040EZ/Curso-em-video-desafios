'''Desenvolva uma lógica que leia o peso ea altura da pessoa,
calcule seu IMC e mostre seu status - de acordo com o seu resultado do IMC'''

peso = float(input('Nos informe o seu peso atual (Em Kg): ' ))
alt  = float(input('Agora informe a sua altura (em Metros ): ' ))

imc = float(float(peso / (alt ** 2)))

if imc < 18.5:
    print('Seu Resultado do IMC foi de {:.2f}, sua Classificação: ABAIXO DO PESO IDEAL ' .format(imc))
elif  18.5 <= imc <= 24.9:
    print('Seu Resultado do IMC foi de {:.2f}, sua Classificação: PESO IDEAL ' .format(imc))
elif 25 <= imc <= 29.9:
    print('Seu Resultado do IMC foi de {:.2f}, sua Classificação: SOBREPESO ' .format(imc))
elif 30 <= imc <= 34.9:
    print('Seu Resultado do IMC foi de {:.2f}, sua Classificação: OBESIDADE GRAU I ' .format(imc))
elif 35 <= imc <= 39.9:
    print('Seu Resultado do IMC foi de {:.2f}, sua Classificação: OBESIDADE GRAU II ' .format(imc))
elif imc >= 40:
    print('Seu Resultado do IMC foi de {:.2f}, sua Classificação: OBESIDADE III ' .format(imc))