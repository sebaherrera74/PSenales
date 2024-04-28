import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def lineal_system_example(x):
    #-x(n)/2    
    #Esto es algo llamado de la listas embebidas. Nos ahorramos un for y es super intuitivo.
    return np.array([ 0.5*(-1.0*item) for item in x])


#Ejemplo de un sistema lineal
f = 10#En Hz
tmin = 0.0
tmax = 1.0
#Por ejemplo samplemosla a 400 Hz para tener 400 puntos.
t   = np.linspace(tmin,tmax,400)

#x=amplitud*seno(frecuencia*tiempo+fase)
#matlab arreglo tiempo ---> transfro 
x_1 = np.sin(2*np.pi*f*t)
#print(t)
#print(x_1)

y_1 = lineal_system_example(x_1)
#print(y_1)

#Nos fijamos que sean del mismo tipo.
print(len(x_1))
print(type(y_1))

plt.figure(figsize=(10,6))

#Graficamos la forma de onda.
plt.plot(t,x_1)
plt.plot(t,y_1)
plt.grid()
plt.xlabel("Tiempo[s]")
plt.ylabel("Amplitud[V]")
plt.legend(["Entrada X1","Salida Y1"])
plt.show()


#Analisis de la señal en el dominio de la frecuencia 
#entra una señal senoidal a un sistema lineal
#Cantidad de muestras de la señal.
n = len(x_1)     #Explicar aqui que hace len 
print (n)

freqz            = np.fft.fftfreq(n,1/n)
freqz            = freqz[range(n//2)]

x_1_spectrum     = fft(x_1)


x_1_abs_spectrum = (2.0/n)*np.abs(x_1_spectrum)
x_1_abs_spectrum = x_1_abs_spectrum[range(n//2)]



y_1_spectrum     = fft(y_1)
y_1_abs_spectrum = (2.0/n)*np.abs(y_1_spectrum)
y_1_abs_spectrum = y_1_abs_spectrum[range(n//2)]


#Ahora graficamos el espectro
plt.figure(figsize=(10,6))
plt.plot(freqz,x_1_abs_spectrum)
plt.plot(freqz,y_1_abs_spectrum)
plt.grid()
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Magnitud")
plt.legend(["Entrada X1","Salida Y1"])
plt.show()


#Vamos a dibujar a x_2
#Ejemplo de un sistema lineal
f = 20 #En Hz
tmin = 0.0
tmax = 1.0
#Por ejemplo samplemosla a 400 Hz para tener 400 puntos.
t   = np.linspace(tmin,tmax,400)
x_2 = np.sin(2*np.pi*f*t)
y_2 = lineal_system_example(x_2)

#Nos fijamos que sean del mismo tipo.
#print(len(x_2))
#print(type(y_2))

#Graficamos la forma de onda.
plt.figure(figsize=(10,6))
plt.plot(t,x_2)
plt.plot(t,y_2)
plt.grid()
plt.xlabel("Tiempo[s]")
plt.ylabel("Amplitud[V]")
plt.legend(["Entrada X2","Salida Y2"])
plt.show()


#Cantidad de muestras de la señal.
n = len(x_2)
freqz            = np.fft.fftfreq(n,1/400)
freqz            = freqz[range(n//2)]

x_2_spectrum     = fft(x_2)
x_2_abs_spectrum = (2.0/n)*np.abs(x_2_spectrum)
x_2_abs_spectrum = x_2_abs_spectrum[range(n//2)]

y_2_spectrum     = fft(y_2)
y_2_abs_spectrum = (2.0/n)*np.abs(y_2_spectrum)
y_2_abs_spectrum = y_2_abs_spectrum[range(n//2)]


#Ahora graficamos el espectro
plt.figure(figsize=(10,6))
plt.plot(freqz,x_2_abs_spectrum)
plt.plot(freqz,y_2_abs_spectrum)
plt.grid()
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Magnitud")
plt.legend(["Entrada X2","Salida Y2"])
plt.show()


#Linealidad de las salida
# Y(n) = T(X1(n)) + T(X2(n))
y = y_1 + y_2
x = x_1 + x_2

#Graficamos la forma de onda. En el tiempo.
plt.figure(figsize=(10,6))
plt.plot(t,x)
plt.plot(t,y)
plt.grid()
plt.xlabel("Tiempo[s]")
plt.ylabel("Amplitud[V]")
plt.legend(["Entrada X1 + X2","Salida Y1 + Y2"])
plt.show()


#Hacemos algo similar a el espectro
n = len(x)
freqz            = np.fft.fftfreq(n,1/400)
freqz            = freqz[range(n//2)]

x_spectrum     = fft(x)
x_abs_spectrum = (2.0/n)*np.abs(x_spectrum)
x_abs_spectrum = x_abs_spectrum[range(n//2)]

y_spectrum     = fft(y)
y_abs_spectrum = (2.0/n)*np.abs(y_spectrum)
y_abs_spectrum = y_abs_spectrum[range(n//2)]

#Ahora graficamos el espectro
plt.figure(figsize=(10,6))
plt.plot(freqz,x_abs_spectrum)
plt.plot(freqz,y_abs_spectrum)
plt.grid()
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Magnitud")
plt.legend(["Entrada X1 + X2","Salida X2 + Y2"])
plt.show()


