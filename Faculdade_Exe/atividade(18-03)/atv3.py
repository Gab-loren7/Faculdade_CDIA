'''
3. Use o método input para ler dois números do teclado e informe qual número é o maior

ex: Digite um número: 5

Digite outro número: 7

7 é o maior número
'''

valor1Recebido = int(input("Digite um número! "))
valor2Recebido = int(input("Digite outro número! "))

print("Calculando...")

if valor1Recebido > valor2Recebido:
    print(f'{valor1Recebido} é o maior número.')
elif valor1Recebido < valor2Recebido:
    print(f'{valor2Recebido} é o maior número.')
elif valor1Recebido == valor2Recebido:
    print(f'{valor1Recebido} é igual a {valor2Recebido}.')
    


    