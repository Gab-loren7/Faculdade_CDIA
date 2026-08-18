'''
6. Imprima todos os números pares de 1 a 200 usando for.
'''

conjunto = range(1,201)
for i in conjunto:
    if i % 2 == 0:
        print(i, end=' ')