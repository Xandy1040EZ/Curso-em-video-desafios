nome = str(input('Digite os seu nome: ')).strip()
print('Fazendo a análise do seu nome ... ')
print('Seu nome em todas as letras Maiúsculas: {} '.format(nome.upper())) #Colocando em letras Maiúsculas
print('Seu nome com todas as letras minúsculas: {} '.format(nome.lower()))#Colocando em letras Minúsculas
print('Seu nome têm no total {} letras '.format(len(nome) - nome.count(' '))) #Contagem das letras exeto os espaços pela função count
prim = nome.split() #O Split faz a quebra dos nomes por meio do espaço e cria uma lista []
print('Seu primeiro nome é {} e têm no total {} letras '.format(prim[0], len(prim[0]))) #Selecionando o primeiro nome da lista[0]

# Feito após a aula de correção