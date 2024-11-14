import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import CubicSpline


# Datos proporcionados
x = np.array([0.3, 0.6, 1.0, 1.3, 1.7, 2.1, 3.1])
y = np.array([0.1500, 0.3293, 0.3679, 0.3543, 0.3106, 0.2572, 0.1397])

# Crear el spline cúbico basado en los datos proporcionados
spline_cubico = CubicSpline(x, y)

# Generar puntos para graficar el spline
x_plot = np.linspace(min(x), max(x), 500)
y_plot = spline_cubico(x_plot)

# Graficar los puntos originales y el spline cúbico
plt.figure(figsize=(8, 5))
plt.plot(x_plot, y_plot, label='Spline Cúbico', color='green')
plt.scatter(x, y, color='red', label='Datos originales')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación con Spline Cúbico')
plt.legend()
plt.grid(True)
plt.show()
