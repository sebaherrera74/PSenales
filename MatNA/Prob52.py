import numpy as np

# Definimos los puntos (x, y)
x = np.array([-0.50, 0.00, 0.25, 1.00])
y = np.array([0.732, 1.000, 1.268, 1.718])

# Número de intervalos
n = len(x) - 1

# Calcular los h_i
h = np.diff(x)

# Construir las matrices para el sistema
A = np.zeros((n + 1, n + 1))
b = np.zeros(n + 1)

# Llenar la matriz A y el vector b
A[0, 0] = 1  # Condición en el primer extremo
A[n, n] = 1  # Condición en el segundo extremo

for i in range(1, n):
    A[i, i-1] = h[i-1]  # h_i-1
    A[i, i] = 2 * (h[i-1] + h[i])  # 2*(h_i-1 + h_i)
    A[i, i+1] = h[i]  # h_i

# Construir el vector b
for i in range(1, n):
    b[i] = (3 / h[i]) * (y[i+1] - y[i]) - (3 / h[i-1]) * (y[i] - y[i-1])

print(A)
print(b)

# Resolvemos el sistema
M = np.linalg.solve(A, b)

# Coeficientes de la spline cúbica
coefficients = []
for i in range(n):
    a = y[i]
    b = M[i]
    c = (1 / (3 * h[i])) * (M[i+1] - M[i])
    d = (M[i] / (2 * h[i])) - (1 / (3 * h[i])) * (M[i+1] + 2 * M[i])
    coefficients.append((a, b, c, d))

print(coefficients)
