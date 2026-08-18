
nomes =  ['Joao','Gabriel','Lucas','Fernando',
         'Rafael','Heitor','Sofia','Fernanda',
         'Pedro','Jesus']

materias = ['calculo','arquitetura de sistemas', 'logica e programacao']

import pandas as pd
import random

with open('dadosPandas.csv', 'w') as arq: ## abre o arq.CSV
    
    arq.write('Nome,Materia,Notas\n') ## Escreve o Cabeçario
    
    for nome in nomes:
        for materia in materias:
            nota = random.random() * 10
            arq.write(f'{nome},{materia},{nota:.1f}\n')
            
df = pd.read_csv('dadosPandas.csv') ## Aqui ele está lendo os dados do arq.csv
print(df)

media = df['Notas'].mean() ## Média das notas
print(f'\n# Filtrando Notas Acima de {media:.1f} ...\n') # jAcima da Média 
print(df[df['Notas'] > media]) ## print dos dados filtrados

print(f'\n# Filtrando Notas Abaixo de {media:.1f} ...\n') # Abaixo da Média
print(df[df['Notas'] < media]) ## print dos dados filtrados

maior_Nota = df['Notas'].max() ## Maior nota
idx_Maior_Nota = df['Notas'].argmax()
nome_Maior_Nota = df['Nome'][idx_Maior_Nota]
print(f'\n# Filtrando Aluno {df['Nome'][idx_Maior_Nota]} / Maior Nota: {maior_Nota} / posição {idx_Maior_Nota} ...\n')
print(df[df['Notas'] == maior_Nota])

menor_Nota = df['Notas'].min() ## Menor nota
idx_Menor_Nota = df['Notas'].argmin()
nome_Menor_Nota = df['Nome'][idx_Menor_Nota]
print(f'\n# Filtrando Aluno {df['Nome'][idx_Menor_Nota]} / Menor Nota: {menor_Nota} / posição {idx_Menor_Nota} ...\n')
print(df[df['Notas'] == menor_Nota])
