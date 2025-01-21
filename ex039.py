#Verificação de Alistamento ao serviço militar

idade = int(input('Qual é a Sua Idade?  '))

if idade == 18:
    print('Já está no momento de você se apresentar ao alistamento militar! ')
elif idade > 18:
    print('Você passou {} anos para se fazer o alistamento ao serviço militar,'
          'procure o serviço militar para se regularizar '
          .format(idade - 18))
else:
    print('Você precisa aguardar {} anos para se alistar ao serviço militar! ' .format(18 - idade))