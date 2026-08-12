'''Crie um programa que leia um tupla comvárias palavras (Sem Acentos) Depois disso, você deve mostrar. para cada palvara,
quais são as suas vogais'''

# Criando uma tupla com várias palavras (sem acento)
palavras = ('Teclado', 'Mouse', 'cafe',
            'perfume', 'carro','caneca',
            'python', 'super', 'mercado',
            'futuro', 'estudar', 'curso',
            'programar', 'linguagem', 'gratis')

# Laço de repetição para percorrer cada palavra da tupla
for p in palavras: #analise da tupla
    print(f'\nNas Palavra {p.upper()} temos', end='') #print com as palavras dentro da var. p formatada para letras maiusculas
    # Laço interno: percorre cada letra da palavra atual
    for letra in p:
        # Converte a letra para minúscula e verifica se é uma vogal
        if letra.lower() in 'aeiou':
            # Se for vogal, imprime na tela
            print(letra, end=' ')



'''
Anotaçôes
Tupla → serve para armazenar várias palavras, não pode ser alterada.

for p in palavras → percorre cada palavra da tupla.

p.upper() → deixa a palavra em maiúsculas só para exibir formatado.

for letra in p → percorre cada letra da palavra.

letra.lower() in 'aeiou' → garante que a comparação funcione mesmo que a letra seja maiúscula.

print(letra, end=' ') → imprime cada vogal encontrada na mesma linha.
'''