#Calculo de la norma de una matriz del problema 3-1 
#del curso maatematica numerica avanzada 

import numpy as np

# Definir la matriz del sistema
A = np.array([[0.003, 59.14], [5.291, -6.13]])

# Calcular la norma de la matriz A
norm_A = np.linalg.norm(A, ord=np.inf)

# Calcular la inversa de la matriz A
A_inv = np.linalg.inv(A)

# Calcular la norma de la matriz inversa
norm_A_inv = np.linalg.norm(A_inv, ord=np.inf)

# Calcular el número de condición
cond_number = norm_A * norm_A_inv
print(cond_number)
