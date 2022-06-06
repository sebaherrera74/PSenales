import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as sig

'''
scipy.signal.firwin(numtaps, # Largo del filtro
                    cutoff, # Frecuencia(s) de corte
                    window='hamming', # Función de ventana
                    pass_zero=True, # Se explicará a continuación
                    fs=None # Frecuencia de muestreo
                    ...
                    )

El argumento pass_zero es un booleano que indica si la frecuencia cero pasa 
o se rechaza por el filtro. Se darán más detalles en los ejemplos que se 
muestran a continuación.

La función firwin retorna un arreglo con h que corresponde a la respuesta 
al impulso del filtro FIR. Luego podemos usar el arreglo h para convolucionar
con nuestra señal de entrada.

'''

fc = 1000 # Frecuencia de corte
Fs = 8000 # Frecuencia de muestreo
L = 2000+1 # Largo del filtro
N=512

h = sig.firwin(L, fc, window='hamming', pass_zero='lowpass', fs=Fs)
freq, H = sig.freqz(h, fs=Fs)

#plt.plot(range(len(h)), h)  
plt.plot(freq, np.absolute(H))  

plt.grid()
plt.show() 

#Probemos si filtra 

# señal en el tiempo $
Tmax=4
t = np.arange(0,Tmax, 1/Fs)
x = np.sin(2*np.pi*300*t)+np.sin(2*np.pi*3000*t)  #Probar cambiando la frecuenciamas alta
X = np.fft.fft(x,N)
# salida del filtro
y=np.convolve(x,h)
Y = np.fft.fft(y,N)
#Grafica en el tiempo de la entrada y de la salida 

plt.figure(figsize=(15,5))
#plt.plot(x[0:2000], label="señal de entrada")
plt.plot(y[1000:5000], linewidth=3, label="señal de salida")
plt.legend()
plt.grid()
plt.show() 
