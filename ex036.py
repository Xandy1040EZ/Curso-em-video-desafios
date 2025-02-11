'''Análise de empréstimo bancário para compra de imóvel'''

#Colhendo Informações
nome = input(str('Qual o seu nome: '))
valor = int(input('Qual o valor do imóvel que deseja financiar? R$ ' ))
print('O Valor do Imovel é de R${:,.2f} ' .format(valor))
renda = int(input('Qual é a sua renda por mês? R$ ' ))
print('A sua renda é de R${:,.2f} ' .format(renda))
tempo = int(input('Em quantos anos, pretente fazer o financiamento? '))
print('Você está planejando em quitar em {} anos ' .format(tempo))

#fazendo as formulas
meses = tempo * 12
parc = valor / meses
print('Seu financiamento ficará em R${} parcelas ' .format(meses))
print('O valor da parcela é {:.2f} ' .format(parc))

#Regra para o financiameto não comprometer mais do que 30% da renda
if parc <= (renda *0.30):
    print('{} PARABÉNS SEU FINANCIAMENTO FOI APROVADO!!!! ' .format(nome))
else:
    print('{} Infelizmente não foi possível o seu financimento! ' .format(nome))
