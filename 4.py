__author__ = 'Rezende'

#Matricula : 1201978 Nome :Joao Pedro Dos Santos Rezende

print ('Quantos watts tem a lampada ?')
lampada = int (input())
print ('Qual a largura do comodo ?')
largura = int (input())
print ('Qual o comprimento do comodo ?')
comprimento = int (input())

area = largura * comprimento
potencia = area * 18
resultado = potencia / lampada

print (resultado)