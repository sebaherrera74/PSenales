import numpy as np
#Ejercicio del problema 3-5 del TP 3 del curso 
#Matematica numerica avanzada
# Definir el sistema de ecuaciones
A = np.array([[4, 3, 0],
              [3, 4, -1],
              [0, -1, 4]])
b = np.array([24, 30, -24])

# Definir parámetros para el método de Gauss-Seidel y Relajación
omega = 1.25
tolerancia = 1e-5
max_iter = 1000

# Definir la función de Gauss-Seidel
def gauss_seidel(A, b, x0, tolerancia, max_iter):
    n = len(b)
    x = np.copy(x0)
    for k in range(max_iter):
        x_old = np.copy(x)
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - suma) / A[i][i]
        # Comprobar la norma infinito del vector diferencia
        if np.linalg.norm(x - x_old, np.inf) < tolerancia:
            return x, k
    return x, max_iter

# Definir la función del método de Relajación (SOR)
def sor(A, b, x0, omega, tolerancia, max_iter):
    n = len(b)
    x = np.copy(x0)
    for k in range(max_iter):
        x_old = np.copy(x)
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (1 - omega) * x[i] + omega * (b[i] - suma) / A[i][i]
        # Comprobar la norma infinito del vector diferencia
        if np.linalg.norm(x - x_old, np.inf) < tolerancia:
            return x, k
    return x, max_iter

# Valores iniciales
x0 = np.array([1, 1, 1])

# Resolver usando Gauss-Seidel
sol_gauss_seidel, iter_gauss_seidel = gauss_seidel(A, b, x0, tolerancia, max_iter)

# Resolver usando SOR (relajación)
sol_sor, iter_sor = sor(A, b, x0, omega, tolerancia, max_iter)

print("La solucion mediante el metodo gauss-seidel:", sol_gauss_seidel)
print("Las iteraciones del metodo gauss-seidel:",iter_gauss_seidel)
print("La solucion mediante el metodo de Relajacion :",sol_sor)
print("Las iteraciones del metodo de Relajacion:",iter_sor)
