nota1 = float(input('Qual foi a nota 1? '))
nota2 = float(input('Qual foi a nota 2? '))
print('Nota 1 foi de {} '.format(nota1))
print('Nota 2 foi de {} '.format(nota2))
print('A média do aluno é de {} '.format((nota1 + nota2)//2))

if 7 <= (nota1 + nota2)//2:
    print('Aluno APROVADO')
else:
    print('Aluno REPROVADO!')

"""Desenvolva um programa que leia as duas notas de um aluno, calcule e
mostre a média"""