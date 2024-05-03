import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#funcion que me crea una señal senoidal le paso como parametro la frecuencia , amplitud y fase
# y Frecuencia de muestreo 
#devuelve un arreglo con los valores del seno calculado y el tiempo en 1 segundo .
#No puedo sumar dos señales porque el arreglo que me devuelve es diferente 

def Senoidal(frecuencia,amplitud,fase,frecmuestreo):
    tmin = 0.0
    tmax = 1.0
    t   = np.linspace(tmin,tmax,frecmuestreo)
    signal=amplitud*np.sin(2*np.pi*frecuencia*t+fase)
    return (signal , t)

#funcion que me crea una señal senoidal le paso como parametro la frecuencia , amplitud y fase
# y Frecuencia de muestreo 
#devuelve un arreglo con los valores del seno calculado y el tiempo en 1 segundo .
#No puedo sumar dos señales porque el arreglo que me devuelve es diferente 

def Coseno(frecuencia,amplitud,fase,frecmuestreo):
    tmin = 0.0
    tmax = 1.0
    t   = np.linspace(tmin,tmax,frecmuestreo)
    signal=amplitud*np.cos(2*np.pi*frecuencia*t+fase)
    return (signal , t)

    
    

#Funcion que me permite graficar una señal
#paso como parametros el tiempo y la señal 
def plot_Signaltime(t,senal):
    plt.plot(t,senal)
    plt.grid()
    plt.xlabel("Tiempo[s]")
    plt.ylabel("Amplitud[V]")
    plt.legend(["Señal"])
    plt.show()

#Funcion que me permite graficar 2 señales en un mismo grafico
#paso como parametros el tiempo y señal1 y señal2 
def plot_2Signaltime(t,senal1,senal2):
    plt.plot(t,senal1)
    plt.plot(t,senal2)
    plt.grid()
    plt.xlabel("Tiempo[s]")
    plt.ylabel("Amplitud[V]")
    plt.legend(["Señal"])
    plt.show()

#Funcion que me grafica en espectro de fourier de 1 señal  
#le paso como parametro el tiempo y la señales x.
def plot_spectrumSignal(x):
   #Graficamos el espectro de la señal
    n = len(x)
    freqz            = np.fft.fftfreq(n,1/n)
    freqz            = freqz[range(n//2)]

    x_spectrum     = fft(x)
    x_abs_spectrum = (2.0/n)*np.abs(x_spectrum)
    x_abs_spectrum = x_abs_spectrum[range(n//2)]
           
    #Ahora graficamos el espectro
    plt.figure(figsize=(10,6))
    plt.plot(freqz,x_abs_spectrum)
    plt.grid()
    plt.xlabel("Frecuencia[Hz]")
    plt.ylabel("Magnitud")
    plt.legend(["Entrada","Salida"])
    plt.show()   
    #Lo devolvemos en formato de tupla por si alguien lo necesita
    return (freqz,x_spectrum)

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
