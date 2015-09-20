__author__ = 'Rezende'

#Matricula : 1201978 Nome :Joao Pedro Dos Santos Rezende

print ('Qual seu sexo ? 1 - Feminino, 2 - Masculino')
sexo = int (input())
print ('Qual seu tamanho ? ')
altura = float (input())

if sexo == 1:
    peso = (62.1 * altura) - 44.7
else:
    peso = (72.7 * altura) - 58

print ('Seu peso ideal e : ', peso, ' kg.')