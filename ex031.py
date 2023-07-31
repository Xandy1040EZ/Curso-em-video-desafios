dis = float(input('Qual a distância da sua viagem: '))
print('Sua viagem terá {}Km '.format(dis))
if dis < 200:
    print('A Viagem terá {} Km de distância e a passagem custará R$ {:.2f} '
          .format(dis, dis * 0.50))
else:
    print('A viagem terá {} Km de distância e a passagem custará R$ {} '
          .format(dis, dis * 0.45))


'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200 km,
e R$ 0,45 para viagens mais longas'''