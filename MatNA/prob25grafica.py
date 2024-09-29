import numpy as np
import matplotlib.pyplot as plt

# Definir la función P(x) y su derivada P'(x)
def P(x):
    return x**3 - 2

def P_prime(x):
    return 3 * x**2

# Rango de valores para x
x = np.linspace(-2, 2, 400)

# Evaluar P(x) y P'(x) en el rango de x
y = P(x)
y_prime = P_prime(x)

# Crear la gráfica
plt.figure(figsize=(8, 6))

# Graficar P(x)
plt.plot(x, y, label=r'$P(x) = x^3 - 2$', color='b')

# Añadir una línea horizontal en y = 0 para indicar las raíces
plt.axhline(0, color='black',linewidth=0.5)

# Títulos y etiquetas
plt.title(r'Gráfica de $P(x) = x^3 - 2$')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid(True)

# Mostrar leyenda
plt.legend()

# Mostrar gráfica
plt.show()
