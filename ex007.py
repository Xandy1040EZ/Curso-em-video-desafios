# Desafio 07: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média
nota1 = float(input('Digite a Nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
media = (nota1 + nota2) // 2
print('Nota 1 do aluno é {0} \n' 'Nota 2 do aluno é {1} \n' 'Nota Média é {2} \n'
      .format(nota1, nota2, media))
print('A nota média do aluno é: {}'.format(media,))