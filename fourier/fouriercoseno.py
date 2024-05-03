import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fourier


# Señal coseno
Fs = 1000
f=100
ampitud=1                      
t = np.arange(0, 999, step=1)
#print(t)
s = ampitud*np.cos(2.0*np.pi*(f/Fs)*t) #señal cosenoidal 
plt.plot(t,s,'r')
plt.show()


#f = np.arange(0, 999, step=1) #vector frecuencia 
f = fourier.fftfreq(n=len(s),d=1/Fs)
print(f)

S =fourier.fft(s)
#print (f)
#print(S)                         #Me imprime los valores conplejos de la transformada de Fourier

plt.figure(figsize=(15,5))
#plt.stem(t,s,'r')  
#plt.plot(f,np.real(S), 'r')      #Ojo con esto 
#plt.plot(f,np.imag(S), 'r')     #ojo con esto 
plt.plot(f,abs(S), 'r')  
#plt.xlabel("Frecuencia [Hz]")
#plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()