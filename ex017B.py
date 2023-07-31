from math import hypot
co = float(input('Digite quando mede o cateto oposto: '))
ca = float(input('Digite quando mede o cateto adjacente: '))
hip = hypot(co, ca)
print('O valor da hipotenusa é {:.2f} '.format(hip))

# Segunda forma de executar o calculo da hipotenusa, com a biblioteca math com a função hypot