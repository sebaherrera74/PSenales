#Problema 1-6 apartado B
import numpy as np
import matplotlib.pyplot as plt

import numpy as np

# Definimos la función f(x)
def f(x):
    return np.sqrt(x + 1) - np.sqrt(x)

# Derivada de f(x)
def df(x):
    return 1/(2 * np.sqrt(x + 1)) - 1/(2 * np.sqrt(x))

# Número de condición kappa(x)
def kappa(x):
    return abs(x * df(x) / f(x))

# Generamos valores de x en progresión logarítmica
x_values = np.logspace(0, 6, num=50)  # Progresión logarítmica entre 1 y 10^6 (50 valores)

# Calculamos los valores de f(x) y kappa(x)
f_values = [f(x) for x in x_values]
kappa_values = [kappa(x) for x in x_values]

# Redondeamos los resultados a 4 dígitos significativos
f_values_rounded = [round(val, 4) for val in f_values]
kappa_values_rounded = [round(val, 4) for val in kappa_values]

# Tabulamos los resultados
print(f"{'x':<15} {'f(x)':<15} {'kappa(x)':<15}")
print("-" * 45)
for x, fx, kx in zip(x_values, f_values_rounded, kappa_values_rounded):
    print(f"{x:<15.4e} {fx:<15.4f} {kx:<15.4f}")

"""
# Gráfica de f(x)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, f_values, label='f(x)', color='blue')
plt.xscale('log')
plt.yscale('linear')
plt.title('Gráfica de f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

# Gráfica de kappa(x)
plt.subplot(1, 2, 2)
plt.plot(x_values, kappa_values, label='kappa(x)', color='red')
plt.xscale('log')
plt.yscale('linear')
plt.title('Gráfica de kappa(x)')
plt.xlabel('x')
plt.ylabel('kappa(x)')
plt.grid()
plt.legend()

# Mostrar las gráficas
plt.tight_layout()
plt.show()
"""