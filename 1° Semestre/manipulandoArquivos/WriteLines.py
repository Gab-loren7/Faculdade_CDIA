lista1 = [
    'string1',
    'fulaninho',
    'beltraninho',
    'ciclaninho',
    'teste',
    'blah'
]
with open('arq1.txt', 'w') as p:
    for var1 in lista1:
        p.write(var1 + '\n')

# with open ('arq1.txt', 'w') as p:
#     lista = ['ola', 'classe']
#     for var1 in lista:
#         p.write(var1 + '\n')