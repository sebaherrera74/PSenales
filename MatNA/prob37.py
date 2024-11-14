import numpy as np

def punto_fijo(x1_0, x2_0, tol=1e-4, max_iter=100):
    """Método de Punto Fijo para resolver un sistema no lineal."""
    
    # Inicializar los valores iniciales
    x1, x2 = x1_0, x2_0
    iteraciones = []

    for i in range(max_iter):
        # Calcular los nuevos valores usando las funciones g1 y g2
        x1_new = (x1**2 + x2**2 + 8) / 10
        x2_new = (x1 * x2**2 + x1 + 8) / 10

        # Guardar las iteraciones para análisis
        iteraciones.append((i + 1, x1, x2, x1_new, x2_new))

        # Comprobar convergencia (criterio: cambio menor que la tolerancia)
        if abs(x1_new - x1) < tol and abs(x2_new - x2) < tol:
            break

        # Actualizar los valores para la siguiente iteración
        x1, x2 = x1_new, x2_new

    return iteraciones, (x1, x2)

# Valores iniciales [0.5, 0.5]
x1_0, x2_0 = 0.5, 0.5
iteraciones, solucion = punto_fijo(x1_0, x2_0)

print(iteraciones, solucion)

