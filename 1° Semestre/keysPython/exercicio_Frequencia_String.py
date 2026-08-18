## Crie um programa que receba uma string do usuário.
## Imprima a frequência de cada caractere na string.

valor_String = input('Digite uma String: ')

dict1 = {}

for t in valor_String:
   if t in dict1:
       dict1[t] += 1
   else:
        dict1[t] = 1
print(dict1)
    
    
