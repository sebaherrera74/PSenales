import numpy as np
import matplotlib.pyplot as plt

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

# Valor de x
x = 0.1
# Calcular el valor real de e^x
valor_real = np.exp(x)

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


x = 0.1
# Calcular el valor real de e^x
valor_real = np.exp(x)

# Calcular el error absoluto para n = 5
n = 5
error_absoluto = abs((x ** (n + 1)) / np.math.factorial(n + 1))

# Calcular el error relativo
error_relativo = (error_absoluto / abs(valor_real)) * 100

# Mostrar resultados
print(f"Valor real de e^{x}: {valor_real}")
print(f"Error absoluto (cota) al usar términos hasta x^{n}: {error_absoluto}")
print(f"Error relativo (cota) al usar términos hasta x^{n}: {error_relativo:.6f}%")