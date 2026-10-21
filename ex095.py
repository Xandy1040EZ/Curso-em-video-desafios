'''Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de DETALHES DO APROVEITAMENTO de cada jogador'''

# BLOCO 1: Criando o dicionário e a lista
# Cria as estruturas de dados que serão utilizadas:
# time: armazena todos os jogadores cadastrados.
# jogador: armazena os dados de um jogador.
# partidas: armazena os gols feitos em cada partida.
time = list()
jogador = dict()
partidas = list()

while True:
    # BLOCO 2: Cadastrando o nome do jogador
    # Limpa os dados do jogador anterior e solicita o nome
    # do novo jogador que será cadastrado.
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))

    # BLOCO 3: Perguntando quantas partidas foram jogadas
    # Solicita a quantidade de partidas disputadas pelo jogador
    # e limpa a lista para registrar os gols do novo cadastro.
    total = int(input(f'Quantas Partidas o {jogador["Nome"]} jogou? '))
    partidas.clear()

    # BLOCO 4: Registrando os gols de cada partida
    # Percorre todas as partidas e solicita a quantidade
    # de gols marcados em cada uma delas.
    for cont in range(1, (total + 1)):
        partidas.append(int(input(f'    Quantos gols foram marcados na partida {cont}? ')))

    # BLOCO 5: Guardando os gols e calculando o total
    # Copia a lista de gols para o dicionário do jogador,
    # calcula a soma dos gols e adiciona uma cópia do jogador
    # à lista que contém todos os jogadores cadastrados.
    jogador['gols'] = partidas[:] # : copia da lista gols por partida
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        # Pergunta se o usuário deseja cadastrar outro jogador.
        # Aceita somente as respostas S ou N.
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    # Encerra o cadastro quando o usuário responde N.
    if resp == 'N':
        break

# BLOCO 6: Exibindo o cabeçalho da tabela
# Apresenta os nomes dos campos que serão exibidos
# na tabela de jogadores cadastrados.
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('__' * 40)

# BLOCO 7: Exibindo os jogadores cadastrados
# Percorre a lista time, atribuindo um código numérico
# a cada jogador e exibindo seus dados na tabela.
for k, v in enumerate(time):
    print(f'{k:>3} ' , end='')
    for d in v.values():
        print(f'{str(d): <15}', end='')
    print()

print('__' * 40)

# BLOCO 8: Consultando os dados de um jogador
# Solicita o código do jogador que o usuário deseja consultar.
# O número 999 encerra a consulta.
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break

    # Verifica se o código informado existe na lista.
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}! ')
    else:
        # Exibe o nome do jogador selecionado e detalha
        # a quantidade de gols marcados em cada partida.
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' => Na partida {i + 1}, fez {g} gols.')
        print('--' * 40)

# BLOCO 9: Encerrando o programa
# Exibe uma mensagem de despedida ao finalizar as consultas.
print('<< VOLTE SEMPRE >>')
