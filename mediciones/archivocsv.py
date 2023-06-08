'''Leer un acrhivo .csv '''

import numpy as np 
import matplotlib.pyplot as plt

from scipy.fft import fft, fftfreq

filename = './mediciones/mediciones1.csv'
raw_data = open(filename)

data = np.loadtxt(raw_data, delimiter=",",skiprows=11)
#print(type (data))

#print(data.shape)                  #forma de los datos
fila,columna=data.shape            #Saco filas y columnas 
#print(fila,columna)               
#print(data.size)                   #Cantidad de filas datos en filas xcolumnas 


#print(data[0:10000,0])
x=data[0:10000,0]
#print(x)

#print(data[0:10000,1])
y=data[0:10000,1]

#Grafica de Voltaje en el tiempo
plt.title('Mediciones 555')
plt.xlabel('Tiempo')
plt.ylabel('MiliVolts')
plt.plot(x,y)
plt.show()



N = 10000
# sample spacing
T = 1.0 / N

yf = fft(y)
print(yf)
print(yf.size)

xf = fftfreq(N, T)#[:N//2]
print(xf)
print(xf.size)





plt.plot(xf, np.abs(yf))
plt.xlim(0, 200)
plt.show()

