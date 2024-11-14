import matplotlib.pyplot as plt
import numpy as np

# Nodos
x_nodos = np.array([0, 1, 2, 3])
y_nodos = np.array([2.5, 7.0, 5.5, 7.0])

# Curva de Bézier cúbica (paramétricas)
t_vals = np.linspace(0, 1, 100)
x_bezier = 3 * t_vals
y_bezier = 9 * t_vals**3 - 18 * t_vals**2 + 13.5 * t_vals + 2.5

# Gráfica
plt.figure(figsize=(8, 6))

# Graficar curva de Bézier cúbica
plt.plot(x_bezier, y_bezier, label='Curva de Bézier Cúbica', color='r')

# Graficar nodos
plt.plot(x_nodos, y_nodos, color='k', zorder=5, label='Nodos')

# Configuración de la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curva de Bézier Cúbica con Nodos')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
