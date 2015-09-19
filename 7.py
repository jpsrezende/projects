__author__ = 'Rezende'

print ('Nota da V1 ? ')
v1 = int (input())
print ('Nota da V2 ? ')
v2 = int (input())
print ('Nota da V3 ? ')
v3 = int (input())

if v3 > 0:
    if v3 > v2:
        temp = v3
        media = (v1 + v3) / 2
    else:
        temp = v2
        media = (v2 + v3) / 2
else:
    media = (v1 + v2) /2

if media >= 6:
    print ('Media : ', media, 'Voce foi aprovado')
if media < 3:
    print ('Media : ', media, 'Voce foi reprovado')
if media > 3 and media < 6:
    print ('Media : ', media, 'esta de exame')