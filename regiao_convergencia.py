import matplotlib.pyplot as plt
import numpy as np

# Criação do gráfico
plt.figure(figsize=(8, 6))

# Eixos
plt.axvline(0, color='black', linewidth=1)  # Eixo imaginário
plt.axhline(0, color='black', linewidth=1)  # Eixo real

# Polos e zeros
plt.scatter([-1, -2], [0, 0], marker='x', color='red', label='Polos')  # Polos
plt.scatter([-3], [0], marker='o', color='blue', label='Zero')  # Zero

# ROC
plt.axvline(-1, color='green', linestyle='--', label='ROC: Re(s) > -1')
plt.fill_betweenx([-5, 5], -1, 5, color='yellow', alpha=0.3, label='ROC')

# Ajustes do gráfico
plt.xlim(-4, 2)
plt.ylim(-2, 2)
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.title('Diagrama de Polos e Zeros com ROC')
plt.legend()
plt.grid(True)
plt.show()