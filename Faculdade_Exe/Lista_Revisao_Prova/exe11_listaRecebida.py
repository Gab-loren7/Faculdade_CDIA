'''
11. Faça uma função que receba uma lista de números e retorne o maior valor.
'''

def maiorDaListaNumeros():
    lista = input('Digite varios numeros : (exe 1234)\n')
    listaArray = []
    
    for i in lista.split(','):
        listaArray += i
    print(f'O maior número da lista é {max(listaArray)}: {listaArray}')
maiorDaListaNumeros()