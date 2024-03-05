import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

# Genera datos de ejemplo (x, y) para la interpolación
x = np.linspace(0, 10, 20)
print(x)
y = np.sin(x)  # Ejemplo: usando una función senoidal
print(y)

# Realiza la interpolación utilizando un spline cúbico
spline = InterpolatedUnivariateSpline(x, y, k=3)
#print(spline)
# Genera nuevos valores de x para evaluar
x_new = np.linspace(0, 10, 100)

# Evalúa el spline en los nuevos valores de x
y_new = spline(x_new)

# Grafica los datos originales y el spline interpolado
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label="Datos Originales", color="blue")
plt.plot(x_new, y_new, label="Spline Interpolado", color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Interpolación con Spline Cúbico")
plt.legend()
plt.grid(True)
plt.show()
