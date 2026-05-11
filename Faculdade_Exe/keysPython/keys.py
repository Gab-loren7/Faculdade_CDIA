var1 = {
    'joao': 21,
    'pedro': 22,
    'camila': 34
}

for nome in var1.keys():
    idade = var1[nome]
    print(f'{nome} tem {idade} anos')