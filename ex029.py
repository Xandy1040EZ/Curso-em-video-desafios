vel = float(input('Qual a velocidade do seu veículo em Km/h: '))
if vel >= 80:
    print('Você Ultrapassou a velocida permitida nesta via, você receberá um multa de R${:.2f} '
          .format((vel - 80) * 7))
else:
    print('Muito bem, continue sua viagem sem ultrapassar os limites de velocidades estabelecidos!!!')
# Escreva um programa que leia a velocidade de um carro. Se a ela ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite
