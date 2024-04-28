import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def non_lineal_system_example(x):
    # x(n)^2    
    #Esto es algo llamado de la listas embebidas. Nos ahorramos un for y es super intuitivo.
    return np.array([ item*item for item in x])

def plot_time_signal(t,x,y):
    #Graficamos la forma de onda en el tiempo
    plt.figure(figsize=(10,6))
    plt.plot(t,x)
    plt.plot(t,y)
    plt.grid()
    plt.xlabel("Tiempo[s]")
    plt.ylabel("Amplitud[V]")
    plt.legend(["Entrada","Salida"])
    plt.show()
    
def plot_spectrum(x,y):
   #Graficamos el espectro de la señal
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
    plt.legend(["Entrada","Salida"])
    plt.show()   
    #Lo devolvemos en formato de tupla por si alguien lo necesita
    return (freqz,x_spectrum,y_spectrum)

#Ejemplo de un sistema No lineal
f_1  = 10 #En Hz
f_2  = 20 #En Hz
tmin = 0.0
tmax = 1.0
#Por ejemplo samplemosla a 400 Hz para tener 400 puntos.
#Tener en mente que que le aplicamos la transformacion x(n)^2
t   = np.linspace(tmin,tmax,400)
x_1 = np.sin(2*np.pi*f_1*t)
y_1 = non_lineal_system_example(x_1)


x_2 = np.sin(2*np.pi*f_2*t)
y_2 = non_lineal_system_example(x_2)

#Hacemos el plot de la señal X1
plot_time_signal(t,x_1,y_1)

rv = plot_spectrum(x_1,y_1)

#Hacemos el plot de la señal X2
plot_time_signal(t,x_2,y_2)
rv = plot_spectrum(x_2,y_2)


#Hacemos el plot de la señal T(X1) + T(X2)
plot_time_signal(t,x_1 + x_2,y_1 + y_2)
rv = plot_spectrum(x_1 + x_2 ,y_1 + y_2)