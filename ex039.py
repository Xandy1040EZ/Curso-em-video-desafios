#Verificação de Alistamento ao serviço militar
from datetime import date     #importe da biblioteca para buscar o ano atual automaticamente
import sys
#Colhendo as informações do usuário
atual = date.today().year
nasc = int(input('Ano de nascimeto: '))
idade = atual - nasc
sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
if sexo == 'F':
    print('Você não precisa de apresentar ao Serviço Militar de forma obrigatória!')
sys.exit()

print('Quem nasceu no ano de {} tem a idade de {} em {}. ' .format(nasc, idade, atual))

# mensagens a serem mostradas ao usuario de acordo com a sua idade
if idade == 18: # se
    print('Você tem {} anos, portanto deve se apresentar ao Serviço Militar o mais breve possível!!! ' .format(idade))
elif idade < 18: #Se nao, se
    saldo = 18 - idade
    ano = atual + saldo
    print('Você tem {} anos, portanto deve se apresentar ao Serviço Militar, deve aguardar {} anos! ' .format(idade, saldo))
    print('Seu alistamento será em {} ' .format(ano) )

elif idade > 18: #Se não
    saldo = idade - 18
    ano1 = atual - saldo
    print('Você tem {} anos, portanto seu prazo de se apresentar ao Serviço Militar já passou em {} anos! ' .format(idade, saldo))
    print('Seu alistamento foi em {} ' .format(ano1))




