import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft


fo=1        #Frecuencia de la continua
T=1000         #Largo temporal
Fs = 100   #Frecuencia de muestreo, probar cambiando las FS

t=np.arange(0,T,step=1/Fs)

signal = np.cos(2.0*np.pi*fo*t)
freq = sfft.fftshift(sfft.fftfreq(n=len(t), d=1/Fs))  #me saca las frecuencias para la escala de las mismas
SA = sfft.fftshift(np.absolute(sfft.fft(signal)))     #SAca la transformada 
plt.figure(figsize=(15,5))
plt.plot(freq,SA, 'r')  
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 
#Analizar que es lo que pasa con la fo=1,23 porque me aparecen los
#picos en -0.75 y +0.75 ?
