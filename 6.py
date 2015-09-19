__author__ = 'Rezende'

print ('Odometro inicial ?')
inicio = int (input())
print ('Odometro final ?')
fim = int (input())
print ('Combustivel gasto ?')
combustivel = int (input())
print ('Valor recebido no dia ?')
valor = int (input())

media = ((inicio - fim) / combustivel)
lucro = ((combustivel * 1.90) - valor)

print ('Lucro : ',lucro)
print ('Media : ', media)