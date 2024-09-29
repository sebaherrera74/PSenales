import math

# Definimos las funciones g1, g2, g3, g4 y g5

def g1(x):
    return x - x**3 - 4*x**2 + 10

def g2(x):
    return math.sqrt((10/x) - 4*x) if x != 0 and (10/x - 4*x) >= 0 else None

def g3(x):
    return 0.5 * math.sqrt(10 - x**3) if (10 - x**3) >= 0 else None

def g4(x):
    return math.sqrt(10/(4 + x)) if (4 + x) != 0 else None

def g5(x):
    return x - (x**3 + 4*x**2 - 10)/(3*x**2 + 8*x) if (3*x**2 + 8*x) != 0 else None

# Iteración de punto fijo con control numérico
def punto_fijo_controlado(g, x0, tol=1e-6, max_iter=1000):
    iteraciones = 0
    x_n = x0
    while iteraciones < max_iter:
        try:
            x_next = g(x_n)
            if x_next is None or not math.isfinite(x_next):
                return float('inf')  # Evitar overflow o indefiniciones
            if abs(x_next - x_n) < tol:
                break
            x_n = x_next
            iteraciones += 1
        except (ValueError, OverflowError, ZeroDivisionError):
            return float('inf')  # Manejar errores numéricos
    return iteraciones

# Valores iniciales
x0 = 1.5
tolerancia = 1e-6

# Número de iteraciones para cada función g(x)
iter_g1 = punto_fijo_controlado(g1, x0)
iter_g2 = punto_fijo_controlado(g2, x0)
iter_g3 = punto_fijo_controlado(g3, x0)
iter_g4 = punto_fijo_controlado(g4, x0)
iter_g5 = punto_fijo_controlado(g5, x0)

# Imprimir resultados
print(f"g1(x): {iter_g1} iteraciones")
print(f"g2(x): {iter_g2} iteraciones")
print(f"g3(x): {iter_g3} iteraciones")
print(f"g4(x): {iter_g4} iteraciones")
print(f"g5(x): {iter_g5} iteraciones")
