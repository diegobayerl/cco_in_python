# código de exemplo CCO
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

#criação da cco
def characteristic_curve(n, p):
    x = np.arange(0, n+1)       # Vetor com valores randomicos
    y = 1 - binom.cdf(x, n, p)  # Subtrai os valores de 1 para inverter a curva
    return x, y

#plotando gráfico no python para a identificação
def plot_characteristic_curve(n, p):
    x, y = characteristic_curve(n, p)
    
    plt.plot(x, y, 'b--', label="CCO")
    plt.title("Curva de Características de Operações")
    plt.xlabel("Número de defeitos")
    plt.ylabel("Probabilidade de rejeição")
    plt.style.use('classic')
    
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso
n = 20  # Número de itens inspecionados
p = 0.1  # Probabilidade de um item ser defeituoso

plot_characteristic_curve(n, p)

#https://gepac.github.io/2019-05-17-intro-matplotlib/
#https://matplotlib.org/stable/api/index.html
