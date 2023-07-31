#Faça um programa que leia a largura e a altura de uma parede em metros(M), calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
#pinta uma área de 2M2

lar = float(input('Digite a largura da parede em Metros: '))
alt = float(input('Digite a altura da parede em Metros: '))
area = lar * alt
print('A área total da parede a ser pintada é de {}m². '.format(area))
tinta = area / 2
print('A quantidade de tinta necessária para pintar a parede é de {} litros de tinta.'.format(tinta))