import numpy as np
import pandas as pd
#Script que me permite encontrar la raiz de una funcion mediante 
#el metodo de Newton
# Defino la funcion y su derivada 
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

# Defino una funcion qu aplica ese metodo en el cual 
#Paso como parametro el valor inicial, la tolerancia que lo saco de la cantidad de 
#cifras significativas, y la iteraccion maxima 

# Define Newton's method
def newton(x0, tol, max_iter):
    iterations = [x0]
    for n in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        iterations.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return iterations

# Set tolerance and maximum iterations
tol = 1e-6
max_iter = 100

newton_iterations = newton(1, tol, max_iter)
print(newton_iterations)

results = pd.DataFrame({
    'Newton': newton_iterations })
print(results)

