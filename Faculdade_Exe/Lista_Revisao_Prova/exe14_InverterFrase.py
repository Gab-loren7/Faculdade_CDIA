'''
14. Inverta uma string digitada pelo usuário.
'''

def inverterString():
    frase = input('Digite uma frase: ')
    letras_Separada = []

    indice = 0
    while indice < len(frase):
        letras_Separada.append(frase[indice])
        indice += 1
    print(letras_Separada)
    frase_Invertida = letras_Separada[::-1]
    print(frase_Invertida)
    print(frase[::-1])
inverterString()