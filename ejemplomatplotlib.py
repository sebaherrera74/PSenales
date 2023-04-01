import matplotlib.pyplot as plt
import numpy as np

#x=np.arange(1,20,50)
#print(x)
#y=x+500
#print(y)
#plt.figure(1,figsize=(6,4.5))  #Tamaño del grafico
 
#plt.plot(x,y,'red',marker="o")                  #hasta aqui no me grafica nada si no pomgo show 
#plt.show()

#genera una señal ruidosa
#y1=0.01*(np.random.randn(100))
#print(y1)
#plt.plot(y1) 
#plt.show()


#plot(x, y, color=’blue’, linestyle=’solid’, marker=’o’, linewidth=1,
#     markerfacecolor=’blue’,markersize=12).

'''
   #linestyle
    "-" o "solid": línea sólida (es la opción por defecto)
    "--" o "dashed": línea discontinua (la mostrada en In [13])
    "-." o "dashdot": línea que alterna guiones y puntos
    ":" o "dotted": línea de puntos
    "None", " " o "": no muestra nada.

'''


x = np.arange(0,100,0.01)
y1 = np.cos(2*np.pi*10*x)
y2 = 5*np.sin(x)


#plt.plot(x,y1)

plt.plot(x,y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.show()


# https://interactivechaos.com/es/manual/tutorial-de-matplotlib/la-funcion-plot-estilo-oo 