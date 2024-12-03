import numpy as np

# Función a integrar
def f(x):
    return np.exp(-x**2 / 2)

# Método de Romberg
def romberg_integration(func, a, b, tol=1e-5):
    # Inicializamos la tabla de Romberg
    R = [[0.5 * (b - a) * (func(a) + func(b))]]  # Primer término (método del trapecio básico)
    n = 1
    while True:
        # Calcular R[n][1] usando el método del trapecio refinado
        h = (b - a) / 2**n  # Tamaño del paso
        summation = sum(func(a + (2 * k - 1) * h) for k in range(1, 2**(n-1) + 1))
        R.append([0.5 * R[n-1][0] + h * summation])  # Refinamiento del trapecio
        #print(R)
        # Completar la fila de extrapolación
        for k in range(1, n + 1):
            R[n].append(R[n][k-1] + (R[n][k-1] - R[n-1][k-1]) / (4**k - 1))
        
        # Verificar si la precisión se cumple
        if abs(R[n][n] - R[n-1][n-1]) < tol:
            return R[n][n], R  # Devolver el valor de la integral y la tabla completa
        n += 1

# Parámetros
a, b = 0, 3
tolerance = 1e-5

# Calcular la integral usando Romberg
integral, romberg_table = romberg_integration(f, a, b, tol=tolerance)
print(romberg_table)
# Factor de escala
factor = 1 / np.sqrt(2 * np.pi)
scaled_integral = factor * integral

print(integral, scaled_integral)

