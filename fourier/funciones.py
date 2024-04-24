import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def plot_spectrum(t,x,y):
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
