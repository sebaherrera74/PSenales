import numpy as np
import pandas as pd
#Script que me permite encontrar la raiz de una funcion mediante 
#el metodo de la biseccion 
# Defino la funcion y su derivada 
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

# Defino una funcion que me permite calcular la biseccion 
#Paso como parametro el intervalo [a,b] la tolerancia que lo saco de la cantidad de 
#cifras significativas, y la iteraccion maxima 
#Como resultado me da una lista con los valores calculados de las raices.
def bisection(a, b, tol, max_iter):
    iterations = []
    for n in range(max_iter):
        c = (a + b) / 2
        print(c)
        print(abs(f(c)))
        iterations.append(c)
        if abs(f(c)) < tol or abs(b - a) / 2 < tol: #planteo esta condiciones para salir de la iteracion 
            break
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
    return iterations

# Defino tolerancia y la cantidad de iteracciones 
tol = 1e-6
max_iter = 50

# Run each method
bisection_iterations = bisection(1, 2, tol, max_iter)
print(bisection_iterations)

# Creo una tabla con los resultados 
results = pd.DataFrame({
    'Bisection': bisection_iterations,
    })
print(results)

#Formula p calcular el orden de convergencia 
def estimate_convergence(iterations):
    p = []
    for i in range(2, len(iterations)):
        p_i = np.log(abs(iterations[i] - np.sqrt(2)) / abs(iterations[i-1] - np.sqrt(2))) / \
              np.log(abs(iterations[i-1] - np.sqrt(2)) / abs(iterations[i-2] - np.sqrt(2)))
        p.append(p_i)
    return p

bisection_order = estimate_convergence(bisection_iterations)
print(bisection_order)