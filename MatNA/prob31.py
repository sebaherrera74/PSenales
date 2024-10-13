import numpy as np

# Coeficientes del sistema
A = np.array([[0.003, 59.14],
              [5.291, -6.130]])

# Términos independientes
b = np.array([59.17, 46.78])

# Resolución del sistema Ax = b
x = np.linalg.solve(A, b)

print("Solución:", x)