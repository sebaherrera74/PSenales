import numpy as np
import matplotlib.pyplot as plt
import scipy.fft


# Señal coseno
Fs = 40
t = np.arange(0, 5, step=1./Fs)
s = np.cos(2.0*np.pi*t*1)
# Se crean las frecuencias y se les hace el shift
f = scipy.fft.fftshift(scipy.fft.fftfreq(n=len(s), d=1/Fs))
S = scipy.fft.fftshift(scipy.fft.fft(s))
print (f)
#print(S)                          #Me imprime los valores conplejos de la transformada de Fourier

plt.figure(figsize=(15,5))
#plt.plot(t,s,'r')  
plt.plot(f,np.real(S), 'r')      #Ojo con esto 
#plt.plot(f,np.imag(S), 'r')     #ojo con esto 
#plt.plot(f,S, 'r')  
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()