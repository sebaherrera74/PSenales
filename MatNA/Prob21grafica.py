#Grafica del problema 2-1 
import numpy as np
import matplotlib.pyplot as plt

# Parámetros conocidos
m = 100  # masa en kg
g = 9.8    # gravedad en m/s^2
c = 15     # coeficiente de rozamiento en kg/s

# Definir la función de velocidad en función del tiempo
def v_t(t, m, g=9.8, c=15):
    return (m * g / c) * (1 - np.exp(-c * t / m))

# Generar valores de tiempo t
t_vals = np.linspace(0, 50, 100)  # tiempo de 0 a 20 segundos
v_vals = v_t(t_vals, m)

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(t_vals, v_vals, label=f'm = {m:.2f} kg', color='blue')
plt.title('Velocidad de caída en función del tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.legend()
plt.show()
