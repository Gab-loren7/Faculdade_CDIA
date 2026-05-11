'''
4. Leia três números do teclado e informe qual é o maior.

ex: Número 1:5

Número 2: 8

Número 3:3

O maior número é 8
'''

valor1Recebido = int(input("Digite um número! "))
valor2Recebido = int(input("Digite outro número! "))
valor3Recebido = int(input("Digite terceiro número! "))

if valor1Recebido > valor2Recebido and valor1Recebido > valor3Recebido:
    print(f'{valor1Recebido} é o maior número.')
elif valor2Recebido > valor1Recebido and valor2Recebido > valor3Recebido:
    print(f'{valor2Recebido} é o maior número.')
elif valor3Recebido > valor1Recebido and valor3Recebido > valor2Recebido:
    print(f'{valor3Recebido} é o maior número.')
    
    