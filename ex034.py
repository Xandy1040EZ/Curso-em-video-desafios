salário = float(input('Qual é o valor do seu salário? R$'))
# fazendo a analise se o salário é maior que 1250 ou menor
if salário > 1250:
    # se for maior que 1250
   aumento = (salário * 10/100) + salário # Fórmula da porcentagem em 10% ( 1250 * 10 / 100
                                                                 # chegaremos em 10% de 1250 )
   print('Seu salário antigo era de R${:.2f} com 10% de aumento seu salário atual será de R${:.2f} '
         .format(salário, aumento))
else:
    # se for menor que 1250
    aumento2 = (salário * 15/100) + salário # Fórmula da porcentagem em 15% ( 1250 * 15 / 100
                                                                    # chegaremos em 15% de 1250)
    print('Seu salário antigo era de R${:.2f} com 15% de aumento seu salário atual será de R${:.2f}'
          .format(salário, aumento2))



'''Escreva um programa que pergunte o salário de um funcionário e calcule o 
valor do seu aumento. 
    Para Salário superiores a R$ 1250,00 calcule um salário com aumento de 10%
    Para salário inferiores ou iguais à R$ 1250,00 o aumento será de 15%'''