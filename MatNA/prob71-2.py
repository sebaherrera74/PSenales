import numpy as np
from numpy.polynomial import Polynomial
# Datos proporcionados
x = np.array([4.55, 12.05, 27.05, 40.79, 72.05, 117.05])
y = np.array([120.8, 39.2, 67.4, 103.3, 123.8, 131.7])
# Ajuste con Polynomial.fit de grado 1
p = Polynomial.fit(x, y, 1)
print(p)
# Coeficientes de Polynomial.fit en la escala original
print(p.convert().coef)