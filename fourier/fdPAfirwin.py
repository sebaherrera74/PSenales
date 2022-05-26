import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as sig



fc = 1000 # Frecuencia de corte
Fs =10000 # Frecuencia de muestreo
L = 1000+1 # Largo del filtro

N=512

#window=sig.get_window('hamming',N,True)

#print (Nx)
#print(window)
#Para pasa alto cambia pass_zero=False

h = sig.firwin(L, fc, window='hamming', pass_zero='highpass', fs=Fs)
freq, H = sig.freqz(h, fs=Fs)

#plt.plot(range(len(h)), h)  
plt.plot(freq, np.absolute(H))  

plt.grid()
plt.show() 

#Probemos si filtra 

# señal en el tiempo $
Tmax=4
t = np.arange(0,Tmax, 1/Fs)
x = np.sin(2*np.pi*300*t)+np.sin(2*np.pi*1000*t)  #Probar cambiando la frecuenciamas alta
X = np.fft.fft(x,N)
# salida del filtro
y=np.convolve(x,h)
Y = np.fft.fft(y,N)
#Grafica en el tiempo de la entrada y de la salida 

plt.figure(figsize=(15,5))
#plt.plot(x[0:2000], label="señal de entrada")
plt.plot(y[0:3000], linewidth=3, label="señal de salida")
plt.legend()
plt.grid()
plt.show() 
