import random
import numpy as np
## Exercício 9
'''
Vamos “separar” nossos dados em tabelas, cada uma em um arquivo
CSV separado e ler tudo usando pandas.
1. Crie um dicionário de ID e nome de disciplinas. Ex: disciplinas = {1:
“matemática”, 2: “física”, 3: “português” …}
2. Crie uma lista de nomes. Ex: nomes = [ “Julia”, “Pedro”, “João”…]
3. Abra um arquivo chamado materias.csv para escrita e inclua o
cabeçalho codigo_disciplina, nome_disciplina
4. Para cada item no dicionário do passo 1, inclua uma linha no
arquivo com “chave,valor” do dicionário (que é o código e o nome
da disciplina)
'''
materias = {
    '1' : 'Matematica',
    '2' : 'Portugues',
    '3' : 'Ingles',
    '4' : 'programacao',
    '5' : 'Filosofia'
}

nomes = ['Gabriel','Joao','Mathues','Luiz','Sofia']

with open("materias.csv","w") as arq:
    arq.write('codigo_disciplina,nome_disciplina\n')
    for chave, valor in materias.items():
        arq.write(f'{chave},{valor}\n')
    
## Exercício 10
'''
Vamos “separar” nossos dados de notas:
1. Abra um arquivo chamado notas.csv para escrita e inclua o
cabeçalho aluno,codigo_disciplina,nota.
2. Para cada nome da lista de nomes e para cada chave do dicionário
de disciplinas, inclua uma linha no arquivo com o valor
“nome,chave do dicionário,nota”. Gere a nota usando random de
0 a 10.
'''
with open('notas.csv','w') as arq:
    arq.write('Aluno,Codigo_Disciplina,Nota\n')
    for aluno in nomes:
        for codigo_disciplina in materias.keys():
            nota = random.random() * 10
            arq.write(f'{aluno},{codigo_disciplina},{nota:.2f}\n')


