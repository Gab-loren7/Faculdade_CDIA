import matplotlib.pyplot as plt

nomes = ['Matemática','Física','Inglês','História']
notas = [7.3,6.7,8.8,9.2]

## .barh gráfico na Horizontal
g = plt.barh(nomes,notas, color='blue')
## Adicionar valores nas Barras
plt.bar_label(g,notas)
plt.show()