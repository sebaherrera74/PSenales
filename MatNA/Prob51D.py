import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import CubicSpline, PchipInterpolator

# Datos proporcionados
x = np.array([0.3, 0.6, 1.0, 1.3, 1.7, 2.1, 3.1])
y = np.array([0.1500, 0.3293, 0.3679, 0.3543, 0.3106, 0.2572, 0.1397])

# 1. Interpolación polinómica de grado 6
polinomio = Polynomial.fit(x, y, deg=len(x) - 1)

# 2. Spline cúbico
spline_cubico = CubicSpline(x, y)

# 3. Interpolación PCHIP (Hermítica)
pchip_interpolador = PchipInterpolator(x, y)

# Puntos para graficar las funciones de interpolación
x_plot = np.linspace(min(x), max(x), 500)
y_polinomio = polinomio(x_plot)
y_spline = spline_cubico(x_plot)
y_pchip = pchip_interpolador(x_plot)

# Graficar las interpolaciones y los nodos originales
plt.figure(figsize=(10, 6))

# Polinomio de grado 6
plt.plot(x_plot, y_polinomio, label='Polinomio (grado 6)', color='blue', linestyle='--')

# Spline cúbico
plt.plot(x_plot, y_spline, label='Spline Cúbico', color='green')

# PCHIP (Hermítica)
plt.plot(x_plot, y_pchip, label='PCHIP (Hermítica)', color='purple', linestyle='-.')

# Nodos originales
plt.scatter(x, y, color='red', label='Datos originales', zorder=5)

# Configuración de la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparación de Métodos de Interpolación')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
