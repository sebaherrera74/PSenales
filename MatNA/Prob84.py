import numpy as np

# Nodos y pesos de Gauss-Hermite
n = 10  # Número de nodos para una buena precisión
x, w = np.polynomial.hermite.hermgauss(n)

# Función a integrar
def f(x):
    return x**3 - x**2

# Evaluar la integral utilizando los nodos y pesos
integral = np.sum(w * f(x))
print(integral)
