## Exercício 11
'''
Crie um dicionário a partir do dataframe das matérias. A chave do
dicionário deverá ser o código da matéria e o valor deverá ser o nome
da matéria
'''

import pandas as pd

materias_df = pd.read_csv("materias.csv")

dict_materias = {}

for indice, linha in materias_df.iterrows():
    codigo = linha["codigo_disciplina"]
    nome = linha["nome_disciplina"]
    dict_materias[codigo] = nome

print(dict_materias)

## Modificando o index do dataframe
materias_df = materias_df.set_index("codigo_disciplina")
print(materias_df,'\n')

nome = materias_df.at[1,'nome_disciplina'] # Acessando um registro por indice
linha = materias_df.loc[1] # Acessando uma linha por indice | df.loc (ID linha, ID coluna)
print(nome)
print(linha)

