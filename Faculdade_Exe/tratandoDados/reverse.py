## Crie um programa que recebe uma string como entrada do usuário e imprime a string contrário

str = input('Digite seu nome: \n')
palavraStr = ''
contador = -1

valorPalavra = len(str) + 1

while contador > (valorPalavra) - (valorPalavra) * 2:
    palavraStr += (str[contador])
    contador -= 1
print(palavraStr)


## Crie um programa que recebe uma entrada separada por espaços e imprime a frase invertendo as palavras

# str = input('Digite seu nome: \n')
# arrayStr = str.split()

# print(arrayStr)

# reverse = ''
# contador = -1

# for i in arrayStr:
#     reverse += arrayStr[contador]
#     reverse += ' '
#     contador -= 1
# print(reverse)
