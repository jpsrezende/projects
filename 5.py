__author__ = 'Rezende'

#Matricula : 1201978 Nome :Joao Pedro Dos Santos Rezende

caixas = 2

print ('Qual o comprimento ? ')
comprimento = int (input())
print ('Qual a largura ? ')
largura = int (input())
print ('Qual a altura ? ')
altura = int (input())

area = ((comprimento * altura) * 2) + ((largura*altura) * 2)
resultado = area / caixas

print (resultado)