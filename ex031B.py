# Versão Simplificada
dist = float(input('Qual a distância da sua viagem? '))
print('Você ira fazer uma viagem de {}Km '.format(dist))
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('O Preço da sua passagem será de {:.2f} '.format(preço))

'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200 km,
e R$ 0,45 para viagens mais longas'''