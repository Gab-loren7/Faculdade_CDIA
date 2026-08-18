'''
10. Calculadora simples
Peça dois números, uma operação e mostre seu resultado
ex:

número 1: 10

número 2: 3

operação: *

resultado: 30
'''
import time

valor1 = float(input('Digite um valor! '))
valor2 = float(input('Digite o segundo valor! '))
valorOperador = input('Digite o sinal de um operador (+, -, *, /)! ')

print('Calculando...\n')
time.sleep(.8)

if valorOperador == '+':
    resposta = valor1 + valor2
    print(f'A soma de {valor1} + {valor2} é: {resposta}.')
elif valorOperador == '-':
    resposta = valor1 - valor2
    print(f'A subtração de {valor1} - {valor2} é: {resposta}.')
elif valorOperador == '*':
    resposta = valor1 * valor2
    print(f'A multiplicação de {valor1} x {valor2} é: {resposta}.')
elif valorOperador == '/':
    resposta = valor1 / valor2
    print(f'A divizão de {valor1} ÷ {valor2} é: {resposta}.')
    
    
    