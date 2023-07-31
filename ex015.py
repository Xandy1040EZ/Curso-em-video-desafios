# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km o carro percorreu ? : '))
dias = int(input('Por quantos dias o carro foi alugado ? : '))
cal1 = (km * 0.15)     # calculo do valor dos km, considerando R$0.15 para cada km
cal2 = (dias * 60)     # calculo do valor dos dias, considerando R$60,00 para cada dia
cal = (60 * dias) + (0.15 * km)
print('Valor referente aos km percorrido é R$ {:.2f} '.format(cal1))
print('Valor referente aos dias que o carro ficou locado é R$ {:.2f} '.format(cal2))
print('-' * 65)
print('O valor total à ser pago é de R$ {:.2f} '.format(cal))