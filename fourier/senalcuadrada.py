"""Programa que me permite abrir un archivo .txt de una medicion de una señal cuadrada  
de 1 Khz de frecuencia y +- 5 volts de pico a pico
"""

import numpy as np 
import matplotlib.pyplot as plt

from scipy.fft import fft, fftfreq

filename = "./fourier/cuadrada.txt"

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
x=.4e-6*x
#print(x)
#print(data[0:20000,1])
y=data[0:10000,1]/1000
Maximo=np.max(y)
minimo=np.min(y)
print("El valor maximo es :" ,Maximo)
print("El valor minimo es :" ,minimo)

plt.title('Señal Cuadrada de 1 Khz ')
plt.xlabel('tiempo')
plt.ylabel('Volts')
plt.plot(x,y)
plt.show()


#Analisis de la señal en el dominio de la frecuencia 

n = len(x)     #Explicar aqui que hace len 
print (n)

freqz            = (np.fft.fftfreq(n, 1.0/n))
print(freqz)
print(len(freqz))
freqz            = freqz[range(n//2)]
print(freqz)
print(len(freqz))

x_spectrum     = fft(y)
print(x_spectrum)
print(len(x_spectrum))

x_abs_spectrum = (2.0/n)*np.abs(x_spectrum)
x_abs_spectrum = x_abs_spectrum[range(n//2)]
print(x_abs_spectrum)
print(len(x_abs_spectrum))
#Ahora graficamos el espectro
plt.figure(figsize=(10,6))
plt.plot((freqz/4)*1000,x_abs_spectrum)

plt.grid()
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Magnitud")
plt.legend(["Entrada X1","Salida Y1"])
plt.xlim(0,100000)
plt.show()



