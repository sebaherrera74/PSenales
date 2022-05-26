import numpy as np
import matplotlib.pyplot as plt
import scipy.fft


# Señal coseno
Fs = 10             #Cambiar frecuencia de muestreo y fo
t = np.arange(0, 5, step=1./Fs)
s1 = np.cos(2.0*np.pi*t*1)
s2 = np.cos(2.0*np.pi*t*1.4)
s=s1+s2

T = 100 # Duración de la ventana, cambiar los valores de la ventana y sacar conclusiones

#w = np.zeros_like(t)
#w[np.absolute(t) < T/2] = 1
w=1
St=s*w

# Se crean las frecuencias y se les hace el shift
f = scipy.fft.fftfreq(n=len(St), d=1/Fs)
S = scipy.fft.fft(St)
print (f)
print(len(St))
#print(S)                         #Me imprime los valores conplejos de la transformada de Fourier

plt.figure(figsize=(15,5))
#plt.plot(t,s,'r')  
#plt.plot(f,np.real(S), 'r')      #Ojo con esto 
#plt.plot(f,np.imag(S), 'r')     #ojo con esto 
plt.plot(f,np.abs(S), 'r')  
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()