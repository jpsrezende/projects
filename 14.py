__author__ = 'Rezende'

#Matricula : 1201978 Nome :Joao Pedro Dos Santos Rezende

vetor = [0] * 10

for i in range (10):
    print ("Qual numero deseja inserir ? ")
    vetor[i] = int (input())
    if vetor[i] < 0:
        vetor[i] = 0

print (vetor)