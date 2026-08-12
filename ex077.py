'''Crie um programa que leia um tupla comvárias palavras (Sem Acentos) Depois disso, você deve mostrar. para cada palvara,
quais são as suas vogais'''

palavras = ('Teclado', 'Mouse', 'cafe',
            'perfume', 'carro','caneca'
            'python', 'super', 'mercado'
            'futuro', 'estudar', 'curso',
            'programar', 'linguagem', 'gratis')
vogais = ['a', 'e', 'i', 'o', 'u']


for p in palavras:
    print(f"\nNas palavras: {p.upper()} temos as vogais: ",end='')
    for letra in p.lower():
        if letra in vogais:
            print(letra, end=' ')