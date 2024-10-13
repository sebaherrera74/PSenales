import numpy as np
import pandas as pd

# Definimos la nueva función y su derivada para el método de Newton
def f_new(x):
    return x**2 - 2

def df_new(x):
    return 2*x

# Método de Bisección
def bisection(f, a, b, tol=1e-6, max_iter=100):
    iters = []
    for i in range(max_iter):
        c = (a + b) / 2
        iters.append((i+1, c))
        if abs(f(c)) < tol or abs(b - a) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return iters

# Método de Newton
def newton(f, df, x0, tol=1e-6, max_iter=100):
    iters = []
    x = x0
    for i in range(max_iter):
        iters.append((i+1, x))
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            break
        x = x_new
    return iters

# Método de la Secante
def secant(f, x0, x1, tol=1e-6, max_iter=100):
    iters = [(1, x0), (2, x1)]
    for i in range(2, max_iter):
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iters.append((i+1, x_new))
        if abs(x_new - x1) < tol:
            break
        x0, x1 = x1, x_new
    return iters

# Aplicamos los tres métodos para la nueva función
bisection_iters_new = bisection(f_new, 1, 2)
newton_iters_new = newton(f_new, df_new, 1)
secant_iters_new = secant(f_new, 0.5, 1)

# Creamos DataFrames para los resultados
bisection_df_new = pd.DataFrame(bisection_iters_new, columns=['Iteration', 'x'])
newton_df_new = pd.DataFrame(newton_iters_new, columns=['Iteration', 'x'])
secant_df_new = pd.DataFrame(secant_iters_new, columns=['Iteration', 'x'])

# Mostrar resultados en las tablas
print("Bisección:")
print(bisection_df_new)
print("\nNewton:")
print(newton_df_new)
print("\nSecante:")
print(secant_df_new)

# Valor exacto de la raíz
x_star = np.sqrt(2)

# Función para calcular el orden de convergencia
def convergence_order(iters, x_star):
    orders = []
    for i in range(2, len(iters)):
        e_n1 = abs(iters[i][1] - x_star)
        e_n = abs(iters[i-1][1] - x_star)
        e_n_1 = abs(iters[i-2][1] - x_star)
        if e_n > 0 and e_n_1 > 0:
            p = np.log(e_n1 / e_n) / np.log(e_n / e_n_1)
            orders.append((i+1, p))
    return orders

# Calcular el orden de convergencia para cada método
bisection_order = convergence_order(bisection_iters_new, x_star)
newton_order = convergence_order(newton_iters_new, x_star)
secant_order = convergence_order(secant_iters_new, x_star)

# Convertir resultados en DataFrames para mejor visualización
bisection_order_df = pd.DataFrame(bisection_order, columns=['Iteration', 'Order of Convergence'])
newton_order_df = pd.DataFrame(newton_order, columns=['Iteration', 'Order of Convergence'])
secant_order_df = pd.DataFrame(secant_order, columns=['Iteration', 'Order of Convergence'])

# Mostrar resultados del orden de convergencia
print("\nOrden de Convergencia - Bisección:")
print(bisection_order_df)
print("\nOrden de Convergencia - Newton:")
print(newton_order_df)
print("\nOrden de Convergencia - Secante:")
print(secant_order_df)
