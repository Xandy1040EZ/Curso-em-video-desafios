'''Crie uma tupla preenchida com os 20 times do Campeonato Brasileiro série A, na ordem da tabela de colocação
depois mostre:
obs: tabela do dia 03/09/2025
A) Apenas os 5 primeiros colocados
B) Os Ultimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabetica
D) Em que posição na tabela se encontra o time do CORINTHIANS '''

tabela = ('Flamengo','Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo',
          'Red Bull Bragantino', 'Fluminense', 'Internacional', 'Ceará SC', 'Corinthians',
          'Grêmio', 'Atlético-MG', 'Vasco da Gama', 'Santos', 'EC Vitória', 'Juventude',
          'Fortaleza', 'Sport Recife')

print('-=-'* 18)
print(f'Lista de times Série A: {", ".join(tabela)}')
print('-=-'* 18)
print('Os cinco primeiros times são: ')
print(', '.join(tabela[0:5]))       #[0:5] vai do item da posição 0 até a 5
print('-=-'* 18)
print('Os últimos 4 colocados são: ')
print(', '.join(tabela[-4:]))       #[-4:] vai do item da posição 16 até o final da lista
print('-=-'* 18)
print('Times em ordem alfabetica: ')
print(', '.join(sorted(tabela)))   #[sorted] ordena em ordem alfabetica
print('-=-'* 18)
print(f'O time do Corinthians está na {tabela.index("Corinthians")+1}ª posição')
print('-=-' *18)

#.join para deixar sem as aspas

'''Localizando a posição do Corinthians
time = 'Corinthians'
posicao = tabela.index(time) + 1  #index funciona para descobrir qual é a posição de determinado item da lista (+1 para comecar a ordenar do 1ª e não do 0)
print('O Corinthians está em qual posição?')
print(f'O Corinthians está na {posicao}ª posição do Campeonato Brasileiro' )'''