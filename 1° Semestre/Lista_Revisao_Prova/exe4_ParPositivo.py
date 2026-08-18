'''
4. Escreva um programa que informe se um número é par e positivo ao mesmo tempo.
'''
import time

valor = int(input('Digite um número: '))
print('Calculando...')
time.sleep(.5) # 5000 ms

if valor % 2 == 0 and valor > 0:
    print(f'{valor} é par e positivo.')
elif valor % 2 == 0 and valor < 0:
    print(f'{valor} é par e negativo.')
elif valor % 2 == 1 and valor < 0:
    print(f'{valor} é ímpar e positivo.')
else:
    print(f'{valor} é ímpar e negativo.')



