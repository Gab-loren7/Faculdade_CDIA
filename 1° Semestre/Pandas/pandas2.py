materias = {
    '1' : 'Matematica',
    '2' : 'Portugues',
    '3' : 'Ingles',
    '4' : 'programacao',
    '5' : 'Filosofia'
}

nomes = ['Gabriel','João','Mathues','Luiz','Sofia']

with open("materias.csv","w") as arq:
    arq.write('codigo_disciplina,nome_disciplina\n')
    for chave, valor in materias.items():
        arq.write(f'{chave},{valor}\n')
    
with open('notas.csv','w') as arq:
    arq.write('cabecalho')