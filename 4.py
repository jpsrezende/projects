__author__ = 'Rezende'

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