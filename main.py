import numpy as np
import matplotlib.pyplot as plt

def calculate_acceptance_rate(samples, target_mean, tolerance):
    accepted = np.abs(samples.mean() - target_mean) <= tolerance
    return np.mean(accepted)

# Parâmetros do processo
target_mean = 50.0  # Média alvo
tolerance = 1.0    # Tolerância

# Faixa de valores para a média do processo
mean_values = np.linspace(40.0, 60.0, 100)

# Lista para armazenar as taxas de aceitação
acceptance_rates = []

# Calcular a taxa de aceitação para cada valor de média
for mean in mean_values:
    # Gerar uma amostra de tamanho 100 do processo
    samples = np.random.normal(mean, 5.0, size=100)
    
    # Calcular a taxa de aceitação para a média atual
    acceptance_rate = calculate_acceptance_rate(samples, target_mean, tolerance)
    acceptance_rates.append(acceptance_rate)

# Plotar a Curva Característica de Operação (CCO)
plt.plot(mean_values, acceptance_rates)
plt.axhline(y=0.95, color='r', linestyle='--', label='Nível de Aceitação Desejado')
plt.xlabel('Valor Médio do Processo')
plt.ylabel('Taxa de Aceitação')
plt.title('Curva Característica de Operação (CCO)')
plt.legend()
plt.grid(True)
plt.show()
