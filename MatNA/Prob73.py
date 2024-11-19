import numpy as np
import matplotlib.pyplot as plt
# Coeficientes de las variables en las ecuaciones
A = np.array([
    [5, 25/2, 125/3, 625/4],
    [25/2, 125/3, 625/4, 625],
    [125/3, 625/4, 625, 15625/6],
    [625/4, 625, 15625/6, 78125/7]
])
print (A)
# Vector de términos independientes
B = np.array([-0.124, -0.125, -0.189, -0.38])

# Resolviendo el sistema de ecuaciones
X = np.linalg.solve(A, B)

# Mostrando los resultados
print("Las soluciones son:")
for i, a in enumerate(X, start=0):
    print(f"a{i} = {a:.4f}")



#Defino el  polinomio y grafico 

def model_func(a0, a1, a2, a3,x):
    return a0 +a1*x +a2*np.power(x, 2)+a3*np.power(x, 3)

# Definir la función objetivo de la forma y = x * exp(-2 * x)
def model_func_real(x):
    return x * np.exp(-2 * x)

# Definir el intervalo
x_vals = np.linspace(0, 5, 100)
Px=model_func(-0.0746,0.0074,0.0122,-0.0022,x_vals)
Fx=model_func_real(x_vals)
#print(Px)

# Graficar los datos y el ajuste
plt.figure(figsize=(10, 6))
plt.plot(x_vals, Px, color='blue', label='Valores del Polinomio')
plt.plot(x_vals, Fx, color='black', label='Valores Reales ')
plt.xlabel('x')
plt.ylabel('Valores de la funcion')
plt.title(' Polinomoio de la forma $y = a0 +a1*x +a2*x**2+a3*x**3$')
plt.legend()
plt.grid(True)

plt.show()