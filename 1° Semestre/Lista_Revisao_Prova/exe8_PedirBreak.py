'''
8. Escreva um programa que peça números até o usuário digitar 0 e então mostre a soma deles.
'''

def repeticao():
    soma = 0
    while True:
        valor = int(input('Digite um valor: '))
        if valor != 0:
            soma += valor   
        else:
            print(f'A soma dos valroes é: {soma}')
            break
repeticao()
