'''Faça um programa que leia o SEXO de uma pessoa, mas só ACEITE os valores 'M' e 'F'.
Caso esteja errado peça a digitação novamente até o ter o valor correto! '''

sexo = 'F' or 'M'
while sexo == 'F' or 'M':
    sexo = str(input('Qual é o sexo da pessoa [F/M] ? ')).upper()
    if sexo == 'F':
        print('O Sexo selecionado foi o FEMININO! ')
    elif sexo == 'M':
        print('O Sexo Selecionado foi o MASCULINO! ')
    else:
        print('Digite novamente: ')
