'''
Escreva um programa que permita um usuário inserir dados em um arquivo. Use 'W' como modo de escrita.

O programa deverá terminar quando o usuário pressionar enter sem informar dados. Nesse caso, abra o arquivo como somente leitura e imprima no conteúdo.
'''

with open("arqAtv5.txt", "w") as cursor:
    while True:
        texto = input('Digite um dado: ')
        
        if texto == '':
            break
        else:
            cursor.write(texto + '\n')
        
with open("arqAtv5.txt", "r") as cursor:
    print(cursor.read())
        
    
    