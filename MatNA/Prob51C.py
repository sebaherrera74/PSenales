import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import CubicSpline, PchipInterpolator
# Datos proporcionados
x = np.array([0.3, 0.6, 1.0, 1.3, 1.7, 2.1, 3.1])
y = np.array([0.1500, 0.3293, 0.3679, 0.3543, 0.3106, 0.2572, 0.1397])
# Crear el interpolador PCHIP basado en los datos
pchip_interpolador = PchipInterpolator(x, y)

# Generar puntos para graficar la interpolación PCHIP
x_plot = np.linspace(min(x), max(x), 500)
y_plot = pchip_interpolador(x_plot)

# Graficar los puntos originales y la interpolación PCHIP
plt.figure(figsize=(8, 5))
plt.plot(x_plot, y_plot, label='Interpolación PCHIP (Hermítica)', color='purple')
plt.scatter(x, y, color='red', label='Datos originales')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Hermítica con PCHIP')
plt.legend()
plt.grid(True)
plt.show()
