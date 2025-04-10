'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre:
- A MEDIA de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres tem menos de 20 anos'''
#Variaveis
somaidade = 0
mediaidade = 0
homem_velho = 0
homem_nome = ''
total_mulher_20 = 0

#Coletando os dados das 4 pessoas
for pessoa in range(1, 5):
    print('=-=-=-=- {}° PESSOA =-=-=-=-' .format(pessoa))
    nome = str(input('NOME: ' )).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [ F / M ]: ')).strip()
    somaidade += idade

# Homem mais Velho
    if pessoa == 1 and sexo in 'Mm':
        homem_velho = idade
        homem_nome = nome
    if sexo in 'Mm' and idade > homem_velho:
    # o M e m são para limitar somente em M/m maisculo e minusculo
        homem_velho = idade
        homem_nome = nome

# Quantidade de mulheres abaixo do 20 anos
    if sexo in 'Ff' and idade < 20:
        # o F e f são para limitar somente em F/f maisculo e minusculo
        total_mulher_20 += 1

# Média de Idade do grupo
mediaidade = somaidade / 4

# Respostas da análise
print('=-=-=-=- ANÁLISE DO GRUPO =-=-=-=-')
print('A média de idade do grupo é de {} anos ' .format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(homem_velho, homem_nome))
print('No total temos {} mulher(es), abaixo do 20 anos no grupo ' .format(total_mulher_20))