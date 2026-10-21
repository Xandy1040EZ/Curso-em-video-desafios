'''FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM AA SITUAÇÃO EM UM DICIIOÁRIO.
NO FINAL, MOSTRE O CONTEUDO DA ESTRUTURA NA TELA'''

aluno = dict()
aluno['NOME'] = str(input('NOME: '))
aluno['MÉDIA'] = float(input(f'Média de {aluno["NOME"]}:  '))
if aluno['MÉDIA'] >= 7:
    aluno['SITUAÇÃO'] = 'APROVADO :)'
elif 5 <= aluno['MÉDIA'] < 7:
    aluno['SITUAÇÃO'] = 'RECUPERAÇÃO'
else:
    aluno['SITUAÇÃO'] = 'REPROVADO :('
print('-=' * 20)
for key, value in aluno.items():
    print(f'{key} é igual a {value}')