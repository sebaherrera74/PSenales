import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error



# Cargar los datos desde el archivo
data = np.loadtxt('./MatNA/datosp7.txt')
concentration = data[:, 0]
#print(concentration)
consistency = data[:, 1]
#print(consistency)



# Definir la función objetivo de la forma y = a1 * x^a2 * exp(a3 * x)
def model_func(x, a1, a2, a3):
    return a1 * np.power(x, a2) * np.exp(a3 * x)

# Ajustar los datos a la función objetivo usando regresión no lineal
initial_guess = [1.0, 1.0, 1.0]
params, covariance = curve_fit(model_func, concentration, consistency, p0=initial_guess)

# Extraer los parámetros ajustados
a1, a2, a3 = params

# Calcular la curva ajustada
fitted_curve = model_func(concentration, a1, a2, a3)

# Graficar los datos y el ajuste
plt.figure(figsize=(10, 6))
plt.scatter(concentration, consistency, color='blue', label='Datos experimentales')
plt.plot(concentration, fitted_curve, color='red', label=f'Ajuste: $y = {a1:.4f} x^{{{a2:.4f}}} e^{{{a3:.4f} x}}$')
plt.xlabel('Concentración (% en peso)')
plt.ylabel('Consistencia')
plt.title('Ajuste de consistencia vs. concentración a una curva de la forma $y = a1 x^{a2} e^{a3 x}$')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar los parámetros ajustados
print(a1, a2, a3)

predicted_consistency = model_func(concentration, a1, a2, a3)
r2 = r2_score(consistency, predicted_consistency)
mse = mean_squared_error(consistency, predicted_consistency)
mae = mean_absolute_error(consistency, predicted_consistency)

print("R²:", r2)
print("MSE:", mse)
print("MAE:", mae)