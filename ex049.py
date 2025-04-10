'''Refazer o desafio 009, mostrando a tabuada de um número que o usúario escolher, só que agora usando o laço FOR'''

num = int(input('De qual número é a tabuada que você precisa?' ))
print('VOCÊ ESCOLHEU A TABUADA DO NÚMERO: {} \n ' .format(num))
print ('-=-' * 5)
for c in range (1, 11):
   print(' {} x {:2} = {:2} ' .format(num, c, num * c))
print ('-=-' * 5)
