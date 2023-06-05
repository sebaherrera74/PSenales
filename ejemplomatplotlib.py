import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,20,0.5)
print(x)
print(x.size)
print(len(x))

#np.pi --->valor pi =3,14....

y=x+2
print(y)
z=x*x

print(z)

#plt.figure(1,figsize=(6,4.5))  #Tamaño del grafico
plt.figure(1)
plt.stem(x,y)
plt.ylim([0,22])
plt.xlim([0,20])
plt.xlabel('$valores de x$')
plt.ylabel('$funcion Y $')
plt.title('Ecuacion de la recta')

plt.figure(2)
plt.stem(x,z)
plt.ylim([-10,400])
plt.xlim([0,20])
plt.xlabel('$valores de x$')
plt.ylabel('$funcion z $')
plt.title('Ecuacion de parabola')

plt.show()

#genera una señal ruidosa
#y1=0.01*(np.random.randn(100))
#print(y1)
#plt.plot(y1)
#plt.show()


#plot(x, y, color=’blue’, linestyle=’solid’, marker=’o’, linewidth=1,
#     markerfacecolor=’blue’,markersize=12).
'''

    "-" o "solid": línea sólida (es la opción por defecto)
    "--" o "dashed": línea discontinua (la mostrada en In [13])
    "-." o "dashdot": línea que alterna guiones y puntos
    ":" o "dotted": línea de puntos
    "None", " " o "": no muestra nada.



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

'''