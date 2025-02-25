 ''''Elabbore um programa que calcule o valor do do produto considerando o seu preço normal e forma de pagamento
A vista dinheiro ou pix 10% desconto; A vista no cartão: 5% desconto; em até 2x no cartão: Valor normal;]
3x ou mais no cartão: 20% de jurus'''

print('{:=^40}' .format(' LOJA XANDY '))
preco = float(input('Qual é o valor das Compras: '))
print('Sua Compra ficou no valor de R${:.2f} ' .format(preco))
print(''''Escolha a sua forma de pagamento: 
[1] à vista dinheiro/pix
[2] à Vista cartão 
[3] 2x Cartão 
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a forma de pagamento, desejada? '))

if opcao == 1:
   total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parc = total / 2
    print('Sua Compra será parcelada em 2x de R${:.2f} SEM JUROS' .format(parc))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    quantparc = int(input('Será em quantas parcelas? '))
    parc = total / quantparc
    print('Sua Compra será parcelada em {}x de R${:.2f} COM JUROS' .format(quantparc, parc))
else:
    total = 0
    print('\033[1;41mO OPÇÃO INVALIDA de pagamento, tente novamente \33[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final' .format(preco, total))




