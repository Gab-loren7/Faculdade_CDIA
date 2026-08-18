'''
12. Cria um código que recebe 10 números do usuário e guarda em uma lista apenas os maiores que 50.
'''

lista_Usuario = [
    431,12,45,76,87,
    11,75,76,43,23
]

# SOLUÇÃO 1: Usando FOR
lista_50 = []
for numero in lista_Usuario:
    if numero > 50:
        lista_50.append(numero)

print("Solução com FOR:")
print(f"Números maiores que 50: {lista_50}")
print()

# SOLUÇÃO 2: Usando WHILE
lista_50_while = []
indice = 0
while indice < len(lista_Usuario):
    if lista_Usuario[indice] > 50:
        lista_50_while.append(lista_Usuario[indice])
    indice += 1

print("Solução com WHILE:")
print(f"Números maiores que 50: {lista_50_while}")

print(len(lista_Usuario)) ## output: 10