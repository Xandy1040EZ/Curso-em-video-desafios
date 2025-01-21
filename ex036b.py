''''Análise de empréstimo bancário para compra de imóvel'''

casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação =casa / (anos * 12)
maximo = salário * 30 / 100
print('Para paga uma casa de R${:.2f} em {} anos' .format(casa, anos), end='')
print(' a prestação será de R${:.2f} '.format(prestação))
if prestação <= maximo:
    print('Empréstimo será APROVADO! ')
else:
    print('Empréstimo NEGADO! ')