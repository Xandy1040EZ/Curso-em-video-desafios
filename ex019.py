from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(lista)
print('O aluno sorteado para apagar o quadro foi: {} '.format(sorteado))

#Desafio 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo na tela o nome do escolhido
