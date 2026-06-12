import pandas as pd

materias_df = pd.read_csv("materias.csv")
notas_df = pd.read_csv("notas.csv")

materias_df = materias_df.set_index("Codigo_Disciplina")

dict_notas = {}

for idx, linha in notas_df.iterrows(): # Lendo cada linha da tabela Notas.csv.
    nome = linha['Aluno'] # Pegando o nome do Aluno.
    nota = linha['Nota'] # Pegando a nota do Aluno.
    cod_disciplina = linha['Codigo_Disciplina'] # Pegando código da disciplina daquela linha.
    nome_disciplina = materias_df.at[cod_disciplina, 'Nome_Disciplina'] # Buscando o nome da disciplina pelo código

    if nome not in dict_notas: # Verifica se o aluno ainda não foi
        dict_notas[nome] = [] # essa linha cria uma lista vazia para guardar as notas do Gabriel.

    dict_notas[nome].append([nome_disciplina,nota]) # adiciona dentro da lista do aluno a disciplina e a nota.

for nome,dados_notas in dict_notas.items(): # método .items() pega a chave e o valor de cada item.
    print(f'{nome}: ')
    for nota in dados_notas:
        # nota = ["Matematica", 1.39]
        nome_disciplina = nota[0] # "Matematica" | nome_disciplina = "Matematica"
        nota_disciplina = nota[1] # 1.39 | nota_disciplina = 1.39
        print(f'\t - {nome_disciplina}, {nota_disciplina}')
    print('\n')

