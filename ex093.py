'''Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO JOGADOR DE FUTEBOL
e QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA.
No final, tudo isso será guardado em um DICIONARIO, incluindo o TOTAL DE GOLS feitos durante o campeonato'''

# BLOCO 1: Criando o dicionário e a lista
# jogador: armazena o nome, os gols por partida e o total de gols.
# partidas: armazena a quantidade de gols marcados em cada partida.
jogador = dict()
partidas = list()

# BLOCO 2: Cadastrando o nome do jogador
# Solicita o nome do jogador e armazena no dicionário
# utilizando a chave 'Nome'.
jogador['Nome'] = str(input('Nome do Jogador: '))

# BLOCO 3: Perguntando quantas partidas foram jogadas
# Solicita a quantidade de partidas disputadas pelo jogador.
# O nome é exibido na pergunta utilizando uma f-string.
total = int(input(f'Quantas Partidas o {jogador["Nome"]} jogou?: '))

# BLOCO 4: Registrando os gols de cada partida
# O laço for percorre todas as partidas.
# A função range começa em 1 e vai até total, inclusive.
# A função append adiciona os gols informados à lista partidas.
for cont in range(1, (total + 1)):
    partidas.append(int(input(f'    Quantos gols foram marcados na partida {cont}? ')))

# BLOCO 5: Guardando os gols e calculando o total
# A expressão partidas[:] cria uma cópia da lista de gols.
# A chave 'gols' armazena essa cópia no dicionário.
# A função sum calcula a soma de todos os gols marcados.
jogador['gols'] = partidas[:] # : copia da lista gols por partida
jogador['total'] = sum(partidas)

# BLOCO 6: Exibindo o dicionário completo
# Exibe todos os dados armazenados no dicionário jogador.
# Os separadores ajudam a organizar a visualização.
print('-=' * 30)
print(jogador)
print('-=' * 30)

# BLOCO 7: Exibindo cada chave e seu valor
# O método items() retorna os pares de chave e valor.
# A variável k representa a chave e v representa seu valor.
# O laço percorre todos os elementos do dicionário.
for k, v in jogador.items():
    print(f' - {k} tem o valor {v}')
print('-=' * 30)

# BLOCO 8: Exibindo o desempenho do jogador
# Exibe o nome do jogador e a quantidade de partidas registradas.
# A função len() conta quantos elementos existem na lista de gols.
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')

# A função enumerate() permite obter o índice e os gols de cada partida.
# O índice começa em zero; por isso, soma-se 1 para exibir a partida.
for i, v in enumerate(jogador["gols"]):
    print(f' => Na partida {i + 1}, fez {v} gols.')

# Exibe o total de gols marcados em todas as partidas.
print(f'Foi um total de {jogador["total"]} gols.')





