'''
10. Crie uma função que receba base e altura e retorne a área de um triângulo.
'''

def areaTriangulo():
    base = int(input(f'Digite um valor para a Base: '))
    altura = int(input(f'Outro para Altura: '))
    
    area = (base * altura) / 2
    
    print(f'A área do triângulo é: {area:.2f}cm')
areaTriangulo()