'''
2. Use o método input para ler do teclado e informe se o número lido é par ou impar

ex: Digite um número: 5
5 é um número impar.
'''
numeroRecebido = int(input('Digite um número!: '))
print('Calculando...')

if numeroRecebido %2 == 0:
    print(f'{numeroRecebido} é um número par.')
elif numeroRecebido %2 == 1:
    print(f'{numeroRecebido} é um número ímpar.')
elif numeroRecebido == 0 :
    print(f'{numeroRecebido} é um número neutro.')
else:
    print(f'{numeroRecebido} não pode ser definido. Tente novamente!')