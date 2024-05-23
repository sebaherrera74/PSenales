from scipy import signal 
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft




Fs = 100     #Cambiar los valores de la frecuencia y observar
t = np.linspace(0, 1, Fs*100, endpoint=False)  
print(t)
s=signal.square(2*np.pi*Fs*t,0.5) 

plt.plot(t,s,'r')  
#plt.ylim(-2, 2)
plt.show()

n = len(s)     #Explicar aqui que hace len 
print (n)

freqz            = np.fft.fftfreq(n,1/(Fs*100))
freqz            = freqz[range(n//2)]

x_1_spectrum     = fft(s)
x_1_abs_spectrum = (2.0/n)*np.abs(x_1_spectrum)
x_1_abs_spectrum = x_1_abs_spectrum[range(n//2)]


#Ahora graficamos el espectro
plt.figure(figsize=(10,6))
plt.plot(freqz,x_1_abs_spectrum)

plt.grid()
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Magnitud")
plt.legend(["Entrada X1","Salida Y1"])
plt.show()

