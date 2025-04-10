'''Faça um pograma que leia um frase e informe se ela é um Palindromo (Pode ser lida de também de trás pra frente)'''

'''Strip para tirar os espaços / upper para jogar a letras para Maiusculas'''
frase = str(input('Digite uma Frase: ')).strip().upper()

'''Split colocando a palavras em uma lista'''
palavras = frase.split()

'''join juntando as palavras sem espaço'''
junto = '' .join (palavras)

'''Fazendo o inverso das letras'''
inverso = ''

'''Primeiro -1 para ele comecar a printar da ultima letra 
   Segundo -1 para ele comerçar antes da primeira letra que é no posição 0
   Terceira -1 para ele ir voltando de uma em uma letra '''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O Inverso da frase {} é {} ' .format(junto, inverso))
if inverso == junto:
    print('A frase é um Palindromo!')
else:
    print('Não é um Palindromo')
