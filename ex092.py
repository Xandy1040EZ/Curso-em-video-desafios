'''Crie um programa que leia NOME ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com idade)
em um DICIONARIO se por acaso a CPTS for diferente de ZERO, o dicionário, receberá também o ano de contratação
 e o Salário. Calcule e acrescente, além da IDADE, com quantos anos a pessoa vai se aposentar'''
from datetime import datetime

# BLOCO 1: Criando o dicionário
dados = dict()
# BLOCO 2: Cadastrando nome e ano de nascimento
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))

# Calculando a idade
idade = datetime.now().year - nasc
dados['Idade'] = idade

# BLOCO 3: Cadastrando a Carteira de Trabalho
dados['CTPS'] = int(input('Carteira de Trabalho (Digite 0 caso não tenha): '))

# BLOCO 4: Verificando se possui Carteira de Trabalho
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))

    # Calculando a idade da aposentadoria
    dados['Aposentadoria'] = dados ['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

# BLOCO 5: Exibindo os dados cadastrados
print('-=' * 30)
for key, value in dados.items():
    print(f' - {key} tem o valor {value}')