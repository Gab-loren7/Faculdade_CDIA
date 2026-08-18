"""
Escreva um código capaz de plotar a função f(x) = x² - 4
- Crie uma função que recebe x e devolve f(x)
- Chame a função para vários valores de x e plote a curva
usando o matplotlib
"""
import matplotlib.pyplot as plt

def func(x: float) -> float:
    return x * x - 4

x = []
y = []
for i in range (-10, 11):
    x.append(i)
    y.append(func(i))

## Adicionando Rótulos aos Eixos
plt.xlabel('eixo X')
plt.ylabel('eixo Y')
## Adicionando Título
plt.title('Gráfico de uma Função Quadrática')

## Adicionando Legenda á Curva (label='')
plt.plot(x,y, label='Exemplo de legenda á curva.')
plt.legend() ## Obrigatório para incorporar legenda

plt.show()

plt.savefig('./MatPlotLib/teste.png')
