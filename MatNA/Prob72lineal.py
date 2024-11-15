import numpy as np
from sklearn.linear_model import LinearRegression

# Cargar los datos desde el archivo
data = np.loadtxt('./MatNA/datosp7.txt')
concentration = data[:, 0]
#print(concentration)
consistency = data[:, 1]
#print(consistency)

# Transformar los datos
X1 = np.log(concentration)
X2 = concentration
Y_prime = np.log(consistency)

# Crear la matriz de variables independientes
X = np.column_stack((X1, X2))

# Ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X, Y_prime)

# Obtener los coeficientes
ln_a1 = model.intercept_
a2, a3 = model.coef_

# Reconstruir a1
a1 = np.exp(ln_a1)

# Calcular los valores predichos
predicted_Y_prime = model.predict(X)
predicted_Y = np.exp(predicted_Y_prime)

# Calcular R² para la bondad del ajuste
from sklearn.metrics import r2_score
r2 = r2_score(consistency, predicted_Y)

# Resultados
print(f"a1 = {a1}, a2 = {a2}, a3 = {a3}")
print(f"R² = {r2}")
