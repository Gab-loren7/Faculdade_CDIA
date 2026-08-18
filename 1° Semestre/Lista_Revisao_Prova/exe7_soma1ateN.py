'''
7. Faça um programa que calcule a soma de todos os números de 1 até N (entrada do usuário).
'''

valor = int(input('Digite um valor máximo: '))

i = 0
soma = 0

while i < valor:
    i += 1
    soma += i

    if i < valor:
        print(i, end=",")
    else:
        print(i, end="")

print(f'\nA soma de 1 até {valor} é: {soma}')