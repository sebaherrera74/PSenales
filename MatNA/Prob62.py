import numpy as np
import matplotlib.pyplot as plt

# Definir el intervalo y la función original
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
f_x = x  # Función original f(x) = x con periodicidad 2π

# Términos de la serie de Fourier
term1 = 2 * np.sin(x)
term2 = -2*np.sin(2 * x)
term3 = 2  * np.sin(3 * x)

# Sumatoria de los primeros tres términos de la serie de Fourier
fourier_approx = term1 + term2 + term3

# Graficar cada término, la sumatoria y la función de origen
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, label='Función Original $f(x) = x$', color='black', linestyle='--')
plt.plot(x, term1, label='Primer término', color='blue')
plt.plot(x, term2, label='Segundo término ', color='orange')
plt.plot(x, term3, label='Tercer término ', color='green')
plt.plot(x, fourier_approx, label='Sumatoria de los términos', color='red')

# Configuración del gráfico
plt.xlabel('$x$')
plt.ylabel('$f(x)$ y términos de la serie')
plt.title('Gráfico de $f(x) = x$ y su Serie de Fourier con los tres primeros términos')
plt.legend(loc='upper right')
plt.grid(True)
plt.ylim(-10, 10)

plt.show()
