#

"""
Para plotear les recomendamos el módulo pyplot de la librería matplotlib, el cual tiene
amplia documentación online. Se suele importar con la abreviación plt.

"""

import matplotlib.pyplot as plt
import numpy as np


#%%Creo vectores ficticios para graficar

Tiempos = np.linspace(0, 25, 1000) #creo un vector de 0 a 25, con 1000 pasos.
Voltaje1 = 5*np.sin(Tiempos) #numpy permite aplicar funciones a arrays hechos en numpy
Voltaje2 = 5*np.cos(Tiempos)

#print(Tiempos)
#print(Voltaje1)
#%% Graficamos y guardamos la figura:

plt.figure()
# graficamos la serie Voltaje1
plt.stem(Tiempos, Voltaje1)
# graficamos, en los mismos ejes la serie Voltaje2
#plt.plot(Tiempos, Voltaje2, color='red', linewidth=1, linestyle='solid', label='Medición 2')
# agregamos una linea vertical al gráfico que marca algo.
#plt.axvline(6.28, color='green', linestyle='dotted', linewidth=1.5, label='Un período')


# Fijamos cuestions cosméticas del grafico: etiquetas, limites, etc.
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
#plt.xlim(0, 25)
#plt.ylim(-6, 9)
#plt.title('Medición de Voltajes')
#plt.legend() #coloca las etiquetas en la mejor posición posible

# guardamos la figura graficada como un archivo
#plt.savefig('graficavoltaje.png', format='png') #esta línea guarda la figura

# trae la figura al frente.
plt.show() 








































