#Prob17
import numpy as np
import matplotlib.pyplot as plt

#Apartado (A)
#Defino 2 funciones una para calcular el valor exponencial 
#y otra para calcular el factorial de un numero 

def calcular_exponencial(x, n):
    suma = 0.0
    for i in range(n):
        suma += (x ** i) / factorial(i)
    return suma

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Valor de x y número de términos
x = 0.1 

#  n numero de terminos entre 2 y 10 para probar diferentes resultados
n = 5

resultado = calcular_exponencial(x, n)
print(f"Valor de e^{x} aproximado usando {n} términos: {resultado}")

#Apartado (B)
# Valor de x
x = 0.1
# Calcular el valor real de e^x
valor_real = np.exp(x)
print(f"Valor Real de e^{x}: {valor_real}")
print(abs(valor_real-resultado))

# Listas para almacenar resultados
num_term = list(range(2, 11))
errores = []

for n in num_term:
    resultado = calcular_exponencial(x, n)
    error = abs(valor_real - resultado)
    errores.append(error)

# Graficar el error de truncación
plt.figure(figsize=(10, 5))
plt.plot(num_term, errores, marker='o')
plt.yscale('log')  # Escala logarítmica para ver mejor el error
plt.title('Error de Truncación en la Aproximación de $e^{0.1}$')
plt.xlabel('Número de Términos (n)')
plt.ylabel('Error de Truncación')
plt.grid(True)
plt.xticks(num_term)
plt.show()


