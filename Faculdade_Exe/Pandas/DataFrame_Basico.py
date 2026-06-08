import pandas as pd

dados = { 
    "Nome" : ["João", "Carlos", "Sabrina", "Camila", "Mara"],
    "Idade" : [22, 35, 21, 34, 47],
    "Salário" : [1000.0,2000.0,3000.0,4000.0,5000.0]
}

df = pd.DataFrame(dados)

print(df,'\n')

## Acessando uma coluna:

col = df["Nome"]

print(col,'\n')

## Acessando uma coluna usando FOR:

for p in col.items():
    print(p)

print('\n') # Apenas para separar conteudo 

## Acessando os items da coluna usando dois parametros em FOR:

for idx, nome in df["Nome"].items():
    print (f"indice: {idx}, Nome: {nome}")