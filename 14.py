__author__ = 'Rezende'

vetor = [0] * 10

for i in range (10):
    print ("Qual numero deseja inserir ? ")
    vetor[i] = int (input())
    if vetor[i] < 0:
        vetor[i] = 0

print (vetor)