## Exercicio 1
'''
1. Crie uma lista contendo 10 nomes de pessoas
2. Crie uma lista contendo 10 salários aleatórios, variando entre 0 e
10.000. Use random para gerar os números
3. Crie um dicionário juntando as duas informações acima.
4. Use o dicionário para criar um dataframe
'''
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
print(df, "\n")


## Exercicio 2
''''
Imprima todos os salários, acessando a coluna correta no dataframe e
iterando sobre o resultado de .items()
'''
col = df["Salario"]
for index, salario in col.items():
    print(f" Indice: {index}, Salario: R$ {salario:.2f}")


## Exercicio 3
''''
Encontre o maior salário. Use o looping for para verificar qual é o
maior salário e imprima seu valor e qual é a posição dele na coluna
'''
maior = 0   #?
index_maior = -1    #?

for i, valor in col.items():
    if maior < valor:
        index_maior = i
        maior = valor
print (f"\nMaior valor: R$ {maior:.2f} na posição: {index_maior}")