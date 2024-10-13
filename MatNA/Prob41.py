import numpy as np

# Datos proporcionados
x = np.array([0.40, 0.50, 0.70, 0.80])
fx = np.array([-0.916291, -0.693147, -0.356675, -0.223144])

# Punto a aproximar
x_approx = 0.60

# Función para calcular el polinomio de Lagrange de grado 3
def lagrange_interpolation(x, fx, x_approx):
    n = len(x)
    result = 0.0

    for i in range(n):
        term = fx[i]
        for j in range(n):
            if j != i:
                term *= (x_approx - x[j]) / (x[i] - x[j])
        result += term

    return result

# Aproximación de ln(0.6)
ln_0_6_approx = lagrange_interpolation(x, fx, x_approx)
print(ln_0_6_approx)
