import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
#from sklearn.metrics import mean_squared_error

# Cargar los datos desde el archivo
data = np.loadtxt('./MatNA/datosp7.txt')
concentration = data[:, 0]
print(concentration)
consistency = data[:, 1]

# Probar diferentes grados de polinomio para encontrar el ajuste óptimo
degrees = range(1, 8)
mse = []
poli=[]
for degree in degrees:
    # Ajuste polinómico
    p = Polynomial.fit(concentration, consistency, degree)
   
    # Evaluación del polinomio ajustado
    #print(p)
    consistency_pred = p(concentration)
    # Calcular el error cuadrático medio (MSE)
    #mse.append(mean_squared_error(consistency, consistency_pred))

# Encontrar el grado óptimo de polinomio con el menor MSE
#optimal_degree = degrees[np.argmin(mse)]
#optimal_polynomial = Polynomial.fit(concentration, consistency, optimal_degree)
print(p)
# Graficar los datos y el ajuste
plt.figure(figsize=(10, 6))
plt.scatter(concentration, consistency, color='blue', label='Datos experimentales')
plt.plot(concentration, consistency_pred , color='red', label=f'Ajuste polinómico ')
plt.xlabel('Concentración (% en peso)')
plt.ylabel('Consistencia')
#plt.title(f'Regresión polinómica de consistencia vs. concentración (grado óptimo: {optimal_degree})')
plt.legend()
plt.grid(True)
plt.show()

# Reportar el grado óptimo y los coeficientes del polinomio
#optimal_degree, optimal_polynomial.coef
