# Importar NumPy 
import numpy as np

# Definimos los puntos vecinos (x_i, y_i, T_i)
points = np.array([
    [1.0, 1.5, 10.00],
    [1.0, 2.0, 10.00],
    [1.0, 2.5, 10.00],
    [1.5, 1.5, 6.81],
    [1.5, 2.0, 4.33],
    [1.5, 2.5, 0.00],
    [2.0, 1.5, 2.00],
    [2.0, 2.0, 0.00],
    [2.0, 2.5, -2.00]
])
#print(points)

# Separar coordenadas y temperaturas
x = points[:, 0]
y = points[:, 1]
T = points[:, 2]
#print(x)
#print(y)
#print(T)

# Matriz A para el sistema Ax = b
A = np.zeros((9, 9))
b = T  # Vector de temperaturas

# Llenamos la matriz A
for i in range(9):
    A[i] = [
        1,               # a_0
        x[i],            # a_1 * x
        y[i],            # a_2 * y
        x[i]**2,         # a_3 * x^2
        y[i]**2,         # a_4 * y^2
        x[i] * y[i],     # a_5 * xy
        x[i]**2 * y[i],  # a_6 * x^2 * y
        x[i] * y[i]**2,  # a_7 * x * y^2
        x[i]**2 * y[i]**2  # a_8 * x^2 * y^2
    ]
#print(A)
# Resolver el sistema de ecuaciones
coefficients = np.linalg.solve(A, b)

print(coefficients)

# Usamos los coeficientes para evaluar la temperatura en (1.3, 2.1)
x_target, y_target = 1.3, 2.1
T_target = (
    coefficients[0] +
    coefficients[1] * x_target +
    coefficients[2] * y_target +
    coefficients[3] * x_target**2 +
    coefficients[4] * y_target**2 +
    coefficients[5] * x_target * y_target +
    coefficients[6] * x_target**2 * y_target +
    coefficients[7] * x_target * y_target**2 +
    coefficients[8] * x_target**2 * y_target**2
)


print(T_target)
