## Crie um programa que contenha um dicionario com o nome do aluno e a nota dele.

## Imprima a lista dos alunos aprovados, interando sobre os itens do dicionario. Obs: O aluno é aprovado quando a nota for maior ou igual a 7.0

Nota_Alunos = {
    'Gabriel' : 8,
    'Chess' : 5.7,
    'Juninho' : 4.9,
    'Heitor' : 10,
    'Jesus' : 7.2
}

for chave in Nota_Alunos.keys():
    nota = Nota_Alunos[chave]
    if nota >= 7.0:
        print(f'Aluno "{chave}" tem média:\t {nota:.1f}\t(+) Aprovado!')
    else:
        print(f'Aluno "{chave}" tem média:\t {nota:.1f}\t(-) Reprovado!')