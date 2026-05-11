'''
6. Peça a idade e classifique a pessoa.

0-12 Criança

13-17 Adolescente

18 ou mais - Adulto
'''
import time

valor1Idade = int(input("Qual a sua idade? "))

print("Ok...")
time.sleep(0.8)
if valor1Idade >= 0 and valor1Idade <= 12:
    print(f'Você é uma criança!')
elif valor1Idade >= 13 and valor1Idade <= 17:
    print(f'Você é um adolescente!')
elif valor1Idade >= 18:
    print(f'Você é um Adulto!')
    
    
