__author__ = 'Rezende'

#Matricula : 1201978 Nome :Joao Pedro Dos Santos Rezende

print ('Data de nascimento ? ')
nascimento = int (input())
idade = 2015 - nascimento

if idade >16:
    print ('Voce tem ', idade, (' anos, voce podera votar este ano !'))
else:
    print ('Voce tem ', idade, ('voce nao podera votar este ano !'))