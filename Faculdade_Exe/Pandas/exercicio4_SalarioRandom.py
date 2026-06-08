import pandas as pd
import random

nomes = ['Joao','Gabriel','Lucas','Fernando',
         'Rafael','Heitor','Sofia','Fernanda',
         'Pedro','Jesus']

salarios = []
for i in range(10):
    salarios.append(random.random() * 10000)

dados = {
    "Nome" : nomes,
    "Salario" : salarios
}

df = pd.DataFrame(dados)
print(df)

col = df["Salario"]
print ("\n",col[0]) # Acessando um elemento da coluna por índice

## Exercício 4
'''
Imprima o nome da pessoa com o maior salário. Use a posição
encontrada no exercício 3 para achar o nome da pessoa.
'''
maior = 0   #?
index_maior = -1    #?

for i, valor in col.items():
    if maior < valor:
        index_maior = i
        maior = valor
print (f"\nMaior valor: R$ {maior:.2f} na posição: {index_maior}")

nome = df['Nome'][index_maior]
print(f"\nA pessoa com o Maior Salário é o {nome} na posição {index_maior}")