## Crie um código capaz de exibir as seguintes curvas:
import matplotlib.pyplot as plt

## Grafico Horizontal
valores_x1 = [0, 1, 2, 3, 4]
valores_y1 = [2, 2, 2, 2, 2]

plt.plot(valores_x1, valores_y1)
plt.show()

## Grafico Vertical
valores_x2 = [2, 2, 2, 2, 2]
valores_y2 = [0, 1, 2, 3, 4]

plt.plot(valores_x2, valores_y2)
plt.show()
