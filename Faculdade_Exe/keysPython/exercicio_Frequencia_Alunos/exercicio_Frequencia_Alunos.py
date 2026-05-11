## Crie um arquivo em que cada linha deverá conter o nome do aluno e sua nota, separados por vírgula.

## Crie um programa que seja capaz de ler essas informações e guardá-las em um dicionário.

## O nome do aluno deverá aparecer mais de uma vez no arquivo.

## Imprima a média do aluno, com base na quantidade de notas que apareceram no arquivo. Imprima a quantidade de notas junto com a média.
dict1 = {}
dict_Quantidade_Vezes = {}

with open('Alunos.txt', 'r') as arq:
    for linha in arq.readlines():
        linha = linha.replace('\n','')
        resultado = linha.split(",")
        
        nome = resultado[0]
        nota = float(resultado[1])
        
        if nome in dict1:
            dict1[nome] = nota
            dict_Quantidade_Vezes[nome] = dict_Quantidade_Vezes[nome] + 1
        else:
            dict1[nome] = nota
            dict_Quantidade_Vezes[nome] = 1
print(dict1)

for nome in dict1.keys():
    soma_Das_Notas = dict1[nome]
    quantidade_De_Notas = dict_Quantidade_Vezes[nome]
    media = soma_Das_Notas / quantidade_De_Notas
    s = ""
    if quantidade_De_Notas > 1:
        s = 's'
    print(f'Aluno(a): {nome}, média: {media:.1f} com {quantidade_De_Notas} nota{s}')