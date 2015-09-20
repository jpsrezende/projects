__author__ = 'Rezende'

import random

def pares():
    for i in range (20):
        num = random.randint (1,100)
        if num % 2 == 0:
            par = num
            return par

vetor = [0] * 20

for i in range (20):
    vetor[i] = pares()
print (vetor)
