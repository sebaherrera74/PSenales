

import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

from scipy.fft import fft, fftfreq

filename = "./pruebainterpolacion1.txt"

raw_data = open(filename)

data = np.loadtxt(raw_data,skiprows=0)



#print(data)
#print(data.shape)
fila,columna=data.shape
#print(fila,columna)
#print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x=data[0:10000,0]
print(x)
print(x.size)
#print(data[0:20000,1])
y=data[0:10000,1]
Maximo=np.max(y)
print("El valor maximo es :" ,Maximo)

plt.title('Simulaciones en SET Vdrain=25mVolts ')
plt.xlabel('Voltage')
plt.ylabel('Corriente')
plt.plot(x,y)
plt.show()

xvals = np.linspace(0,1000,10)
print(xvals)
#yinterp = np.interp(x, y)
#print(yinterp)

"""spline = InterpolatedUnivariateSpline(x, y, k=3)

x_new = np.linspace(0, 10, 100)

# Evalúa el spline en los nuevos valores de x
y_new = spline(x_new)
print(y_new)
plt.plot(x_new, y_new, label="Spline Interpolado", color="red")
plt.show()
"""