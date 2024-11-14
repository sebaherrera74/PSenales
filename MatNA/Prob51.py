import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Datos proporcionados
x = np.array([0.3, 0.6, 1.0, 1.3, 1.7, 2.1, 3.1])
y = np.array([0.1500, 0.3293, 0.3679, 0.3543, 0.3106, 0.2572, 0.1397])

# Ajuste polinómico de mayor orden posible (n = len(x) - 1)
#En este caso deg=6
polinomio = Polynomial.fit(x, y, deg=len(x) - 1)

# Generar puntos para graficar la interpolación
x_plot = np.linspace(min(x), max(x), 500)
y_plot = polinomio(x_plot)

# Graficar los puntos originales y el polinomio de interpolación
plt.figure(figsize=(8, 5))
plt.plot(x_plot, y_plot, label='Interpolación polinómica (grado 6)', color='blue')
plt.scatter(x, y, color='red', label='Datos originales')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Polinómica de Mayor Orden')
plt.legend()
plt.grid(True)
plt.show()
