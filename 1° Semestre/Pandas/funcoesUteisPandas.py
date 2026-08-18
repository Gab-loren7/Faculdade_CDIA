import pandas as pd
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
print(df,'\n')

col = df['Salarios']

print(f'O Maior Salário: {col.max()}') # Puxa o maior valor 
print(f'O Salário medio: {col.mean()}') # Puxa o valor mediano
print(f'O Menor Salário: {col.min()}') # Puxa o menor valor 
print(f'Posição do Maior Salário: {col.argmax()}') # Puxa a posção do maior valor 
print(f'Posição do Menor Salário: {col.argmin()}') # Puxa a posição do menor valor 
print(f'Total de salários: {col.count()}') # Conta a quantidade de valores
print('\n')

## Imprima o nome da pessoa com o maior salário. Use os métodos de coluna para achar a posição com o maior salário.
maior_valor = f'{col.max():.2f}'
posicao_maior_valor = col.argmax()
print(f'O maior valor é do {df['Nomes'][posicao_maior_valor]}: R${maior_valor} na posição {posicao_maior_valor}\n')

## Imprima os nomes das pessoas cujo salário é abaixo da média. use os métodos de coluna para achar a média. use o método de filtro para selecionar os items com salário abaixo da media!

dados = {
    'Nome': ['João', 'Carlos', 'Sabrina', 'Camila', 'Mara'],
    'Idade': [22,35,21,34,47],
    'Salario':[1000.0, 2000.0, 3000.0, 4000.0, 5000.0]
}
df2 = pd.DataFrame(dados) 
print(df2)

print('\n# Valores Filtrados\n')

media = df2['Salario'].mean() #3000
filtro = df2['Salario'] < media
print(df2[filtro])