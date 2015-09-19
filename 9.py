__author__ = 'Rezende'

print ('Quantas macas ? ')
quantidade = int (input())

if quantidade >= 12:
    valor = quantidade * 0.25
else:
    valor = quantidade * 0.30

print ('Valor da compra : ', valor)