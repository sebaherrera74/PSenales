import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fourier


# Señal seno
Fs = 2000
f0=30
t = np.arange(0, 5, step=1./Fs)
s = np.sin(2.0*np.pi*f0*t)
# Se crean las frecuencias y se les hace el shift
f = fourier.fftshift(fourier.fftfreq(n=len(s), d=1/Fs))
S = fourier.fftshift(fourier.fft(s))
#print (f)
#print(S)                          #Me imprime los valores conplejos de la transformada de Fourier

plt.figure(figsize=(15,5))
#plt.plot(t,s,'r')  
#plt.plot(f,np.real(S), 'r')      #Ojo con esto 
#plt.plot(f,np.imag(S), 'r')     #ojo con esto 
plt.plot(f,S, 'r')  
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()