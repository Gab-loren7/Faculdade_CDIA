'''
9. Crie uma função que receba um número e retorne o seu dobro.
'''
import time as t

def dobrarNumero():
    valor = int(input('Digite um valor: '))
    dobro = valor * 2
    
    t.sleep(.8)
    
    print(f'O dobro de "{valor}" é: {dobro}')
dobrarNumero()
    
    