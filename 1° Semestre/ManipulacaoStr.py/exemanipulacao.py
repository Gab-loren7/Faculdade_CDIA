var1 = "Estamos aprendendo a programar em Python"

def count (var1, caractere):
    qnt = 0
    for c in var1:
      if c == caractere:
          qnt += 1
    return qnt
    
print ('O "a" apareceu:', count(var1, 'a'), 'vezes')