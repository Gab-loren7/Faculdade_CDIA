import pandas as pd

# dados = {
#     'Nome': ['João', 'Carlos', 'Sabrina', 'Camila', 'Mara'],
#     'Idade': [22,35,21,34,47],
#     'Salario':[1000.0, 2000.0, 3000.0, 4000.0, 5000.0]
# }

# df = pd.DataFrame(dados)

# print(df,'\n')

# col = df['Nome']

# print(col,'\n')

# for p in col.items():
#     print(p)
    
'''
1. Crie uma lista contendo 10 nomes de pessoas
2. Crie uma lista contendo 10 salários aleatórios, variando entre 0 e
10.000. Use random para gerar os números
3. Crie um dicionário juntando as duas informações acima.
4. Use o dicionário para criar um dataframe
'''

import random

nomes = ['Joao','Gabriel','Lucas','Fernando',
         'Rafael','Heitor','Sofia','Fernanda',
         'Pedro','Jesus']

salarios = []
for i in range(10):
    salarios.append(random.random() * 10000)
    
dados = {'Nomes': nomes,
         'Salarios': salarios}

df = pd.DataFrame(dados)

print(df, '\n')

col = df['Salarios']

# for i,valor in col.items(): # usar dois parametros i(index), valor(salario)
#     print(f'R$ {valor:.2f}')

## Encontre o maior salário. Use o looping for para verificar qual é o maior salário e imprima seu valor e qual é a posição dele na coluna.

maior = 0
idx_maior = -1
for i, valor in col.items():
    if maior < valor:
        maior = valor
        idx_maior = i
print(f"maior valor foi do '{df['Nomes'][idx_maior]}': R${maior:.2f} na posição {idx_maior}")
# Dois chamdo de parâmetro um puxa o valor e o outro o index.

