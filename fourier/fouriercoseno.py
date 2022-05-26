import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fourier


# Señal coseno
Fs = 200  
f=70
ampitud=2                      
t = np.arange(0, 5, step=1./Fs)
s = ampitud*np.cos(2.0*np.pi*f*t)

f = fourier.fftfreq(n=len(s), d=1/Fs)
S =fourier.fft(s)
#print (f)
#print(S)                         #Me imprime los valores conplejos de la transformada de Fourier

plt.figure(figsize=(15,5))
#plt.stem(t,s,'r')  
#plt.plot(f,np.real(S), 'r')      #Ojo con esto 
#plt.plot(f,np.imag(S), 'r')     #ojo con esto 
plt.plot(f,S, 'r')  
#plt.xlabel("Frecuencia [Hz]")
#plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()