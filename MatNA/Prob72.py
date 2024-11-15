import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from scipy.optimize import curve_fit


# Cargar los datos desde el archivo
data = np.loadtxt('./MatNA/datosp7.txt')
concentration = data[:, 0]
#print(concentration)
consistency = data[:, 1]
#print(consistency)

# Grafico los datos obtenidos del archivo.txt
plt.figure(figsize=(10, 6))
plt.scatter(concentration, consistency, color='blue', label='Datos experimentales')
plt.xlabel('Concentración (% en peso)')
plt.ylabel('Consistencia')
plt.legend()
plt.grid(True)
plt.show()


# Probar diferentes grados de polinomio para encontrar el ajuste óptimo
Grado = 5 #Ingresar los diefrentes grados 
p = Polynomial.fit(concentration, consistency, Grado)
   
# Evaluación del polinomio ajustado
    
consistency_pred = p(concentration)
    
#Grafica la curva obtenida y el polinmos esperado

plt.figure(figsize=(10, 6))
plt.scatter(concentration, consistency, color='blue', label='Datos experimentales')
plt.plot(concentration, consistency_pred , color='red', label=f'Ajuste polinómico ')
plt.xlabel('Concentración (% en peso)')
plt.ylabel('Consistencia')
plt.legend()
plt.grid(True)
plt.show()








