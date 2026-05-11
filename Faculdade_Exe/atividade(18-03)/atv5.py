'''
5. Conversor de temperatura

Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.

FÓRMULA: F = (C*9/5) + 32
'''

import time

valorCelsius = int(input("Digite um valor em Celcius! "))

print("Calculando...")
time.sleep(1) # Pause for 1 seconds

valorFahrenheit = (valorCelsius * 1.8) + 32
print(f'{valorCelsius}° Celsius é igual a {valorFahrenheit} Fahrenheit')