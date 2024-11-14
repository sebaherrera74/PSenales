import numpy as np
import matplotlib.pyplot as plt

# Definir el intervalo
x_vals = np.linspace(0, 1, 1000)

# Función original
f_x_vals = np.exp(-2 * x_vals)

# Aproximación de Padé (2,2)

#Ingreso los coeficientes calculados en el Inciso (A)
a0, a1, a2, b1, b2 = 1, -1.9, 1.23, 0.1, -0.56
pade_vals = (a0 + a1 * x_vals + a2 * x_vals**2) / (1 + b1 * x_vals + b2 * x_vals**2)

# Serie de Maclaurin de orden 4
maclaurin_vals = 1 - 2 * x_vals + 2 * x_vals**2 - (4 / 3) * x_vals**3 + (2 / 3) * x_vals**4

# Error absoluto entre f(x) y las aproximaciones
error_pade = np.abs(f_x_vals - pade_vals)
error_maclaurin = np.abs(f_x_vals - maclaurin_vals)

# Graficar las funciones
plt.figure(figsize=(12, 6))

# Subplot de funciones
plt.subplot(1, 2, 1)
plt.plot(x_vals, f_x_vals, label=r'$e^{-2x}$', color='black')

plt.plot(x_vals, pade_vals, label='Padé (2,2)', linestyle='--', color='blue')



plt.plot(x_vals, maclaurin_vals, label='Maclaurin (Orden 4)', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparación de funciones')
plt.legend()
plt.show()

# Subplot de errores
plt.subplot(1, 2, 2)
plt.plot(x_vals, error_pade, label='Error Padé (2,2)', color='blue')
plt.plot(x_vals, error_maclaurin, label='Error Maclaurin (Orden 4)', color='green')
plt.xlabel('x')
plt.ylabel('Error absoluto')
plt.title('Error absoluto de aproximaciones')
plt.legend()

plt.tight_layout()
plt.show()
