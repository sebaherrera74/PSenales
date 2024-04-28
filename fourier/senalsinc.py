"""Programa que me permite abrir un archivo .txt de una medicion de una señal cuadrada  
de 1 Khz de frecuencia y +- 5 volts de pico a pico
"""

import numpy as np 
import matplotlib.pyplot as plt



from scipy.fft import fft, fftfreq

filename = "PSenales/fourier/noise.txt"

raw_data = open(filename)
#print(raw_data)
data = np.loadtxt(raw_data,skiprows=11)

#print(data)
#print(data.shape)
fila,columna=data.shape
#print(fila,columna)
#print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x=data[0:10000,0]
#print(x)
#print(data[0:20000,1])
y=data[0:10000,1]
Maximo=np.max(y)
print("El valor maximo es :" ,Maximo)

plt.title('Señal Cuadrada de 1 Khz ')
plt.xlabel('tiempo')
plt.ylabel('Volts')
plt.plot(x,y)
plt.show()


#Analisis de la señal en el dominio de la frecuencia 
#entra una señal senoidal a un sistema lineal
#Cantidad de muestras de la señal.
n = len(x)     #Explicar aqui que hace len 
print (n)

freqz            = (np.fft.fftfreq(n, 1.0/n))

freqz            = freqz[range(n//2)]

x_spectrum     = fft(y)


x_abs_spectrum = (2.0/n)*np.abs(x_spectrum)
x_abs_spectrum = x_abs_spectrum[range(n//2)]

#Ahora graficamos el espectro
plt.figure(figsize=(10,6))
plt.plot(freqz,x_abs_spectrum)

plt.grid()
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Magnitud")
plt.legend(["Entrada X1","Salida Y1"])
plt.xlim(0,100000)
plt.show()

