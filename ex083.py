'''Crie um programa onde o usuário digite uma expressão qualquer que use, PARÊNTESES. 
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ORDEM CORRETA'''
#Coletando a expressão com o usuário
exp = str(input('Digite uma expressão: '))
#Criando a lista com parenteses
parenteses = []
#laço de repetição
for simb in exp:
    #Validando os parenteses abertos '('
    if simb == '(':
        parenteses.append('(') #adicionando na lista
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop() #Removendo um parenteses da lista
        else:
            parenteses.append(')') #validando caso tenha um parenteses sem o par
            break
#validando se a expressão está de forma correta
if len (parenteses) == 0:
    print('Sua expressão está válida! ')
else:
    print('A sua expressão está inválida! ')


