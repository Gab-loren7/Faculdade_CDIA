## Exercício 7
'''
Crie uma lista de nomes. Ex: nomes = [ “Julia”, “Pedro”, “João”…]
2. Crie uma lista de nomes de disciplinas. Ex: disciplinas =
[“matemática”, “física”, “português” …]
3. Abra um arquivo dados.csv para escrita (w)
4. Escreva o cabeçalho: nome,disciplina,nota
5. Gere 1 linha para cada nome x disciplina, criando uma nota
aleatória com random, de 0 a 10.
'''

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

## Exercício 8
'''
Carregue o arquivo dados.csv em um dataframe e exiba:
1. O aluno com a maior nota
2. O aluno com a menor nota
3. A quantidade de alunos acima da media
4. A quantidade de alunos abaixo da media
Obs: use os métodos de coluna para calcular as estatísticas requisitas
acima.
'''

df = pd.read_csv('dadosPandas.csv') ## Aqui ele está lendo os dados do arq.csv
print(df)

media = df['Notas'].mean() ## Média das notas
print(f'\n# Filtrando Notas Acima de {media:.1f} ...\n') # Acima da Média 
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
