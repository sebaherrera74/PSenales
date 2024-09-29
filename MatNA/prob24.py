import numpy as np

# Definimos la función f(x) y su derivada f'(x)
def f(x):
    return x**2 - np.cos(x)

def df(x):
    return 2*x + np.sin(x)

# Método de Aproximaciones Sucesivas
def aproximaciones_sucesivas(x0, tol=1e-6, max_iter=100):
    iteraciones = 0
    x_prev = x0
    while iteraciones < max_iter:
        x_next = np.sqrt(np.cos(x_prev))  # g(x) = sqrt(cos(x))
        if abs(x_next - x_prev)/abs(x_next) < tol:
            break
        x_prev = x_next
        iteraciones += 1
    return x_next, iteraciones

# Método de Aitken
def aitken(x0, tol=1e-6, max_iter=100):
    iteraciones = 0
    x_prev = x0
    while iteraciones < max_iter:
        x1 = np.sqrt(np.cos(x_prev))
        x2 = np.sqrt(np.cos(x1))
        x_next = x_prev - ((x1 - x_prev)**2) / (x2 - 2*x1 + x_prev)
        if abs(x_next - x_prev)/abs(x_next) < tol:
            break
        x_prev = x_next
        iteraciones += 1
    return x_next, iteraciones

# Método de Steffensen
def steffensen(x0, tol=1e-6, max_iter=100):
    iteraciones = 0
    x_prev = x0
    while iteraciones < max_iter:
        g_x = np.sqrt(np.cos(x_prev))
        g_gx = np.sqrt(np.cos(g_x))
        x_next = x_prev - ((g_x - x_prev)**2) / (g_gx - 2*g_x + x_prev)
        if abs(x_next - x_prev)/abs(x_next) < tol:
            break
        x_prev = x_next
        iteraciones += 1
    return x_next, iteraciones

# Método de Newton
def newton(x0, tol=1e-6, max_iter=100):
    iteraciones = 0
    x_prev = x0
    while iteraciones < max_iter:
        x_next = x_prev - f(x_prev)/df(x_prev)
        if abs(x_next - x_prev)/abs(x_next) < tol:
            break
        x_prev = x_next
        iteraciones += 1
    return x_next, iteraciones

# Parámetros iniciales
x0 = 1
tol = 1e-6

# Ejecutar los métodos
resultado_aprox_sucesivas = aproximaciones_sucesivas(x0, tol)
resultado_aitken = aitken(x0, tol)
resultado_steffensen = steffensen(x0, tol)
resultado_newton = newton(x0, tol)

# Resultado final
# Imprimir resultados
print(resultado_aprox_sucesivas)
print(resultado_aitken)
print(resultado_steffensen)
print(resultado_newton)
