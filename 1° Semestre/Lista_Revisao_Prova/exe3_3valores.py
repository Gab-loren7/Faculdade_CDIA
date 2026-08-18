'''
3. Faça um programa que receba três números e mostre o maior deles
'''

valores = []

var1 = int(input('Digite o valor 1: '))
var2 = int(input('Digite o valor 2: '))
var3 = int(input('Digite o valor 3: '))

valores = var1,var2,var3

print(f'O maior valor é {max(valores)}')