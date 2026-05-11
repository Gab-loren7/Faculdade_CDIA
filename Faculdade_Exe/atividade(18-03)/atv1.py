'''
Use o método input para ler o teclado e informe se o número lido é positivo ou negativo.

ex: Digite um númeor 5
5 é um número positivo
'''

numeroRecebido = int(input('Digite um número!: '))
print('Calculando...')
if numeroRecebido < 0:
    print(f'{numeroRecebido} é um número negativo.')
elif numeroRecebido > 0:
    print(f'{numeroRecebido} é um número positivo.')
elif numeroRecebido == 0 :
    print(f'{numeroRecebido} é um número neutro.')
else:
    print(f'{numeroRecebido} não pode ser definido. Tente novamente!')
    
    