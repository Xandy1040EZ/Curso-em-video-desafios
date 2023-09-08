num = int(input('Escolha um número inteiro: '))
print('\033[1;31;46mO número escolhido foi o {} e o seu antecessor é o {} \033[m'
      .format(num,  num - 1))
print('\033[1;32;44mO número escolhido foi o {} e o seu sucessor é o {} \033[m'
      .format(num, num + 1))

'''Faça um programa que leia um número inteiro e mostre na tela o seu 
antecessor e o seu sucessor'''
