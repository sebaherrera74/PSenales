import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#funcion que me crea una señal senoidal le paso como parametro la frecuencia y amplitud 
#devuelve un arreglo con los valores del seno calculado y el tiempo.
#No puedo sumar dos señales porque el arreglo que me devuelve es diferente 

def buildSenoidal(frecuencia,amplitud,fase):
    tmin = 0.0
    tmax = 1.0
    t   = np.linspace(tmin,tmax,frecuencia*100)
    return (amplitud*np.sin(2*np.pi*frecuencia*t+fase)) , t

#funcion que me crea una señal senoidal le paso como parametro la frecuencia y amplitud 
#devuelve un arreglo con los valores del seno calculado y el tiempo.
def buildCoseno(frecuencia,amplitud):
    tmin = 0.0
    tmax = 1.0
    t   = np.linspace(tmin,tmax,frecuencia*100)
    return (amplitud*np.cos(2*np.pi*frecuencia*t)) , t
    
    

#Funcion que me permite graficar una señal
#paso como parametros el tiempo y la señal 
def plot_time(t,senal):
    plt.plot(t,senal)
    plt.grid()
    plt.xlabel("Tiempo[s]")
    plt.ylabel("Amplitud[V]")
    plt.legend(["Señal"])
    plt.show()
    

#Funcion que me grafica en espectro de fourier de 2 señales 
#le paso como parametro el tiempo y las dos señales x, y.
def plot_spectrum(x,y):
   #Graficamos el espectro de la señal
    n = len(x)
    freqz            = np.fft.fftfreq(n,1/n)
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
