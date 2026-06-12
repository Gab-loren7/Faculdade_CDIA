## Exercício 12
'''
Vamos “juntar” nossos dados manualmente:
1. Abra o arquivo chamado materias.csv como um dataframe
2. Abra o arquivo chamado notas.csv como um dataframe
3. Imprima a lista de alunos e suas notas com o formato:
Aluno, nome da matéria, nota
'''

import pandas as pd

materias_df = pd.read_csv('materias.csv')
notas_df = pd.read_csv('notas.csv')

materias_df = materias_df.set_index('codigo_disciplina') # Troca o index

for idx, linha in notas_df.iterrows():
    nome = linha['Aluno']
    nota = linha['Nota']
    cod_disciplina = linha['Codigo_Disciplina']
    nome_disciplina = materias_df.loc[cod_disciplina]['nome_disciplina']

    print(f"{nome}, {nome_disciplina}, {nota}")