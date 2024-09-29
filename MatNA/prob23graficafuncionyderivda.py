import numpy as np
import matplotlib.pyplot as plt

# Definir la función y su derivada
def f(x):
    return x**2 - np.cos(x)

def df(x):
    return 2*x + np.sin(x)

# Crear el rango de valores de x
x_vals = np.linspace(-2, 2, 400)

# Evaluar la función y su derivada en el rango de x
y_vals = f(x_vals)
dy_vals = df(x_vals)

# Crear la gráfica
plt.figure(figsize=(8,6))

# Graficar la función f(x)
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 - \cos(x)$", color='blue')

# Graficar la derivada f'(x)
plt.plot(x_vals, dy_vals, label=r"$f'(x) = 2x + \sin(x)$", color='red', linestyle='--')

# Añadir una línea horizontal en y=0
plt.axhline(0, color='black',linewidth=0.5)  # Eje horizontal

# Añadir una línea vertical en x=0
plt.axvline(0, color='black',linewidth=0.5)  # Eje vertical

# Configuración del gráfico
plt.title("Gráfica de $f(x)$ y $f'(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Mostrar la gráfica
plt.show()
