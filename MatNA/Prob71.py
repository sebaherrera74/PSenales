import numpy as np 
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Datos proporcionados
x = np.array([4.55, 12.05, 27.05, 40.79, 72.05, 117.05])
y = np.array([120.8, 39.2, 67.4, 103.3, 123.8, 131.7])

# Ajuste polinómico de grado 2 y 
p1=Polynomial.fit(x, y, deg=1)
p2 = Polynomial.fit(x, y, deg=2)
p3 = Polynomial.fit(x, y, deg=3)
p4=Polynomial.fit(x, y, deg=4)
p5=Polynomial.fit(x,y,deg=5)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)


coef_p1 = p1.convert().coef
coef_p2 = p2.convert().coef
coef_p3 = p3.convert().coef
coef_p4 = p4.convert().coef
coef_p5 = p5.convert().coef

print(coef_p1)
print(coef_p2)
print(coef_p3)
print(coef_p4)
print(coef_p5)







# Evaluamos los polinomios ajustados
x_fit = np.linspace(min(x), max(x), 60)
print(x_fit)
y_fit_p1=p1(x_fit)
y_fit_p2 = p2(x_fit)
y_fit_p3 = p3(x_fit)
y_fit_p4 = p4(x_fit)
y_fit_p5 = p5(x_fit)
# Graficamos los datos y los ajustes polinómicos
plt.scatter(x, y, color='blue', label="Datos originales")
plt.plot(x_fit, y_fit_p1, color='yellow', label="Ajuste Polinómico Grado 1")
plt.plot(x_fit, y_fit_p2, color='green', label="Ajuste Polinómico Grado 2")
plt.plot(x_fit, y_fit_p3, color='red', label="Ajuste Polinómico Grado 3")
plt.plot(x_fit, y_fit_p4, color='blue', label="Ajuste Polinómico Grado 4")
plt.plot(x_fit, y_fit_p5, color='black', label="Ajuste Polinómico Grado 5")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Regresión Polinómica")
plt.grid(True)
plt.show()


#Calculo de el Coefeciente de Determinacion y de la Desviacion Estandar

# Número de puntos
n = len(x)

# Calcular el promedio de y
y_mean = np.mean(y)

# Ajuste de un polinomio de grado 5 y convertirlo a la escala original
p_degree_5 = Polynomial.fit(x, y, 1)

# Valores predichos con el polinomio de grado 5
y_pred_degree_5 = p_degree_5(x)

# 1. Calcular R^2 (coeficiente de determinación) para el polinomio de grado 5
ss_total = np.sum((y - y_mean)**2)  # Suma total de cuadrados
ss_res_degree_5 = np.sum((y - y_pred_degree_5)**2)  # Suma de los residuos al cuadrado para el grado 5
r_squared_degree_5 = 1 - (ss_res_degree_5 / ss_total)

# 2. Calcular la desviación estándar de los residuos para el polinomio de grado 5
std_residuals_degree_5 = np.sqrt(ss_res_degree_5 / (n - 5))

print(r_squared_degree_5, std_residuals_degree_5)