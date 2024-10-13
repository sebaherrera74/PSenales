# Funciones G1(x1, x2) y G2(x1, x2) derivadas del sistema de ecuaciones
def G1(x1, x2):
    return (x2**2 + 8) / (10 - x1)

def G2(x1, x2):
    return (x1 * x2**2 + x1 + 8) / 10

# Función que ejecuta el método del punto fijo
def punto_fijo(x1_0, x2_0, tol=1e-6, max_iter=100):
    x1, x2 = x1_0, x2_0
    iteraciones = 0
    
    while iteraciones < max_iter:
        # Guardamos los valores actuales para calcular el error
        x1_new = G1(x1, x2)
        x2_new = G2(x1, x2)
        
        # Calculamos el error relativo
        error_x1 = abs(x1_new - x1)
        error_x2 = abs(x2_new - x2)
        
        # Verificamos si ambos errores son menores que la tolerancia
        if error_x1 < tol and error_x2 < tol:
            print(f"Convergencia alcanzada en la iteración {iteraciones}")
            return x1_new, x2_new, iteraciones
        
        # Actualizamos los valores para la siguiente iteración
        x1, x2 = x1_new, x2_new
        iteraciones += 1
        
        # Mostramos el progreso
        print(f"Iteración {iteraciones}: x1 = {x1_new:.6f}, x2 = {x2_new:.6f}, error_x1 = {error_x1:.6f}, error_x2 = {error_x2:.6f}")
    
    print("Se alcanzó el número máximo de iteraciones sin converger.")
    return x1, x2, iteraciones

# Valores iniciales
x1_0 = 0.5
x2_0 = 0.5

# Ejecutamos el método del punto fijo
sol_x1, sol_x2, iteracion = punto_fijo(x1_0, x2_0)
print(f"Solución final: x1 = {sol_x1:.6f}, x2 = {sol_x2:.6f} en {iteracion} iteraciones")

