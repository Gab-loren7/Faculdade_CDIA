import pandas as pd

materias_df = pd.read_csv("materias.csv")

for indice, linha in materias_df.iterrows(): # Invoca o DataFrame
    # Retorna a coluna índice e a respectiva linha do dataframe
    codigo = linha["codigo_disciplina"]
    nome = linha["nome_disciplina"]
    print(f'{codigo} = {nome}')