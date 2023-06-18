#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar
# Considere: US$ 1,00 = R$ 3.27

reais = float(input('Digite quanto você tem em R$ para saber quantos US$ valem: '))
conv = reais / 3.27 #contação sugerida pelo desafio
print('Em Reais você têm R$ {} em Dólar é equivalente à US$ {:.2f} '.format(reais, conv))
