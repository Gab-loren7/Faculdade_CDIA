'''
13. Conte quantas vogais existem em uma frase digitada.
'''

def contadorVogais():
    frase = input('Digite um frase: ')
    letras_Separadas = []
    vogais_contador= 0
    
    indice = 0
    while indice < len(frase):
        letras_Separadas.append(frase[indice])
        indice += 1
      
    for i in letras_Separadas:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vogais_contador += 1 
    print(f'Nas letras: {letras_Separadas}\nExistem {vogais_contador} vogais.')
contadorVogais()