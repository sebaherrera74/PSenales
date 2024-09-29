#Problema 1.6
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Función f(x)
def f_x(x):
    return np.sqrt(x + 1) - np.sqrt(x)

# Generar una progresión logarítmica de valores de x entre 1 y 10^6
x_values = np.logspace(0, 6, num=50)  # Generamos 50 valores en progresión logarítmica

# Calcular f(x) para cada valor de x y redondear a 4 dígitos significativos
f_values = [round(f_x(x), 4) for x in x_values]

#Grafico 
plt.semilogx(x_values,f_values) #me grafica una escala logaritmica en el eje X
plt.grid()
plt.xlabel("Valores de x ")
plt.ylabel("Funcion")
plt.legend(["sqrt(x + 1) - np.sqrt(x)"])
plt.show()

 


# Crear una tabla con los resultados
tabla = pd.DataFrame({
    'x': x_values,
    'f(x)': f_values
})

# Mostrar la tabla
print(tabla)
