#Faça uma função que duplique os valores das idades

var1 = {
    'joao': 21,
    'pedro': 22,
    'camila': 34
}

def duplicando():
    for chave in var1.keys():
        var1[chave] = 2 * var1[chave]
    return print(f'{var1}\n')
duplicando()        