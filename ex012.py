#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço total do produto R$ '))
desc = preco - (preco * 0.05)
val = preco * 0.05
print('O novo valor do seu produto é de R$ {}, com 5% de desconto. '.format(desc))
print('=' * 60)
print('Seu desconto total com o cupom de 5% foi de R$ {} '.format(val))