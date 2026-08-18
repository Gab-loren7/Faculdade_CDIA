## Modificando elementos de um Dataframe
import pandas as pd

df = pd.DataFrame({
    'codigo' : [1,2,3,4,5],
    'nome' : ["Carlos","Daniel","Ester","Fátima","Gorette"]
})
print(df)

df.at[2,'nome'] = 'Estela' # Modifica 'Ester' por 'Estela'
print(df)

df = df.set_index('codigo') # Troca o index para o valor da colum 'codigo'
print(df)

## Modificando vários elementos de um Dataframe

# df.loc (FILTRO DA LINHA, FILTRO DA COLUNA)

df.loc[2:4, 'nome'] = '(Oculto)'
print(df)

sobrenomes = []
sobrenomes.extend(['Silva', 'Mendes', 'Soares', 'Gomes', 'Oliveira'])
df['sobrenome'] = sobrenomes
print(df)

df.to_json('saida.json')
print(df)