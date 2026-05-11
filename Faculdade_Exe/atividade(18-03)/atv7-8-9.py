'''
7. Contador até N

Peça um número N e mostre todos os números de 1 até N.

Digite um número: 5
1, 2, 3, 4, 5
'''
import time

i = 1
valor1Periodo = int(input('Digite um número para mostrar o seu período! '))
print('Calculando...')
time.sleep(0.5)

while i < (valor1Periodo + 1):
    print(i, end=' ')
    time.sleep(0.2)
    i += 1
print("\nFim!")