'''Crie um Programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS guardando os dados de cada pessoa em um
DICIONARIO e todos os DICIONARIOs em uma LISTA. No final, mostre:

A) Quantas pessoas foram cadastradas;
B) A MÉDIA de idade do grupo;
C) Uma lista com todas as MULHERES;
d) Uma lista com todas as pessoas com IDADE acima da média'''

# BLOCO 1: Criando as listas, o dicionário e as variáveis
# galera: armazena os dados de todas as pessoas cadastradas.
# pessoa: armazena os dados de uma pessoa por vez.
# soma: acumula as idades para calcular a média.
# média: armazenará a média de idade das pessoas cadastradas.
galera = list()
pessoa = dict()
soma = média = 0

# BLOCO 2: Iniciando o cadastro das pessoas
# O laço principal permite cadastrar várias pessoas.
# O dicionário é limpo antes de receber os dados da próxima pessoa.
while True:
    pessoa.clear()

    # Solicita o nome da pessoa.
    pessoa['nome'] = str(input('Nome: '))

    # BLOCO 3: Validando o sexo
    # Solicita o sexo e converte a resposta para maiúscula.
    # Aceita somente M ou F. Caso contrário, exibe uma mensagem de erro.
    while True:
        pessoa['sexo'] =str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')

    # BLOCO 4: Registrando a idade
    # Solicita a idade e adiciona seu valor à variável soma.
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    # Copia os dados da pessoa para a lista galera.
    galera.append(pessoa.copy())

    # BLOCO 5: Perguntando se deseja continuar
    # Permite cadastrar outra pessoa.
    # Aceita somente S ou N e repete a pergunta em caso de erro.
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    # Encerra o cadastro se a resposta for N.
    if resp == 'N':
        break

# BLOCO 6: Exibindo a quantidade de pessoas cadastradas
# len(galera) retorna a quantidade de pessoas armazenadas na lista.
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas. ')

# BLOCO 7: Calculando e exibindo a média de idade
# Divide a soma das idades pela quantidade de pessoas cadastradas.
# O formato 5.2f exibe o resultado com duas casas decimais.
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')

# BLOCO 8: Exibindo as mulheres cadastradas
# Percorre a lista galera e verifica o sexo de cada pessoa.
# Se o sexo for F ou f, exibe o nome correspondente.
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end=' ')
print()

# BLOCO 9: Exibindo as pessoas com idade igual ou superior à média
# Percorre a lista e compara a idade de cada pessoa com a média.
# Se a idade for maior ou igual à média, exibe seus dados.
print('D) Lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('     ' ,end=' ')
        for k, v in p.items():
            print(f' {k} = {v}; ', end='')
            print()

# BLOCO 10: Encerrando o programa
# Exibe uma mensagem de encerramento.
print('<< ENCERRADO >>')