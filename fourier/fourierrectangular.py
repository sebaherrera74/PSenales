import numpy as np
import matplotlib.pyplot as plt
import scipy.fft


# Señal coseno
Fs = 100          #Cambiar los valores de la frecuencia y observar
t = np.arange(0, 5, step=1./Fs) #Aqui defino la cantidad de muestras
s = np.zeros_like(t)
s[np.abs(t)<2] = 1

# Se crean las frecuencias y se les hace el shift
f = scipy.fft.fftshift(scipy.fft.fftfreq(n=len(s), d=1/Fs))
S = scipy.fft.fftshift(scipy.fft.fft(s))
#print (f)
#print(S)                          #Me imprime los valores conplejos de la transformada de Fourier

plt.figure(figsize=(15,5))
#plt.plot(t,s,'r')  
#plt.plot(f,np.real(S), 'r')      #Ojo con esto 
#plt.plot(f,np.imag(S), 'r')     #ojo con esto 
#plt.stem(t,s, 'r')  
plt.stem(f,S, 'r')  
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()