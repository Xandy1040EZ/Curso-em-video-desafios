'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a
média atingida (REPROVADO, RECUPERAÇÃO OU APROVADO:'''

nota1 = float(input("Qual foi a primeira nota do aluno?  "))
nota2 = float(input("Qual foi a segunda nota do aluno?  "))
media = (nota1 + nota2) / 2

if media <= 5.0:
    print("a nota média do aluno foi de {:.1f} portanto o aluno está REPROVADO! :/ " .format(media))
elif 5.0 <= media <= 6.9:
      print("A média do aluno foi de {:.1f} e portanto o aluno está em RECUPERAÇÃO!!!  " .format(media))
else:
    print("A nota média do aluno foi de {:.1f} e o aluno está APROVADO!!! :D " .format(media))
