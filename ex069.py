'''Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada. o programa deverá perguntar
se o USUÁRIO quer continuar e no final mostre
 A) Quantas pessoas tem mai se 18 anos
 B) Quantos HOMENS foram cadastrados
 C) Quantas mulheres tem menos de 20 anos'''
#Variveis que precisaremos
maiores = 0
homem = 0
mulher = 0
mulheres_20 = 0
while True: #laço infinito Principal
    print('#=' *15)
    print('CADASTRE UMA PESSOA')
    print('#=' *15)

    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Informe a Idade: '))
    while True: #Laço infinito validação do Sexo
        sexo = str(input('Informe um sexo Feminino ou Masculino [F / M]: ')).upper().strip()
        if sexo in ('F', 'M'):
            break
        print('Escolha uma opção válida [F / M]')
    #condicionais
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        mulher += 1
    if idade >= 18:
        maiores += 1
    if idade <= 20 and sexo == 'F':
        mulheres_20 += 1

    while True: #Laço de validação da decisao
        decisao = str(input('Quer cadastrar uma nova pessoa? [S / N]')).upper().strip()
        if decisao in ('S', 'N'):
            break
        print('Escolha uma opção válida [S / N]')
    if decisao == 'N':
        break
        print('#=' * 15)
        print('CADASTRO FINALIZADO')
        print('#=' * 15)


print('#=' * 15 )
print('SEGUEM AS ESTATÍSTICAS')
print('#=' * 15)
print(f'Foram cadastradas {maiores} pessoas maiores de idade')
print(f'Foram cadastrados {homem} homens no total')
print(f'Foram cadastrados {mulheres_20} mulheres com idade menor de 20 anos')