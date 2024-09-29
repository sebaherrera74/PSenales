import numpy as np
import pandas as pd
#Script que me permite encontrar la raiz de una funcion mediante 
#el metodo de la secante 
# Defino la funcion y su derivada 
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

# Defino una funcion qu aplica ese metodo en el cual 
#Paso como parametro el valor inicial, la tolerancia que lo saco de la cantidad de 
#cifras significativas, y la iteraccion maxima 

# Define Secant method
def secant(x0, x1, tol, max_iter):
    iterations = []
    for n in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iterations.append(x2)
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    return iterations

# Set tolerance and maximum iterations
tol = 1e-6
max_iter = 100

secant_iterations = secant(0.5, 1, tol, max_iter)
print(secant_iterations)
results = pd.DataFrame({
    'Secant': secant_iterations })
print(results)

#Formula p calcular el orden de convergencia 
def estimate_convergence(iterations):
    p = []
    for i in range(2, len(iterations)):
        p_i = np.log(abs(iterations[i] - np.sqrt(2)) / abs(iterations[i-1] - np.sqrt(2))) / \
              np.log(abs(iterations[i-1] - np.sqrt(2)) / abs(iterations[i-2] - np.sqrt(2)))
        p.append(p_i)
    return p

secant_order = estimate_convergence(secant_iterations)
print(secant_order)