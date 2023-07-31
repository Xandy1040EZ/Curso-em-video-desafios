reais = float(input('Digite quanto você tem em R$: '))
dolar = reais / 4.79  #contação do dia 20/06/2023
euro = reais / 5.23   #contação do dia 20/06/2023

print('R$ {:.2f} são equivalentes à US$ {:.2f} \nR$ {:.2f} são equivalentes á € {:.2f} '
      .format(reais, dolar, reais, euro))
