import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x**2 - np.cos(x)

# Crear el rango de valores de x
x_vals = np.linspace(-2, 2, 400)

# Evaluar la función en el rango de x
y_vals = f(x_vals)

# Crear la gráfica
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 - \cos(x)$")
plt.axhline(0, color='black',linewidth=0.5)  # Eje horizontal
plt.axvline(0, color='black',linewidth=0.5)  # Eje vertical
plt.title("Gráfica de $f(x) = x^2 - \cos(x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
