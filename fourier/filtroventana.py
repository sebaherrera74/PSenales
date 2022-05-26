import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
import scipy.signal 



fc = 0.1 # Frecuencia de corte
fc2=1 
Fs = 1 # Frecuencia de muestreo
n = np.arange(-50, 50, step=1/Fs);
f = scipy.fft.fftshift(scipy.fft.fftfreq(n=len(n), d=1/Fs))

# Diseño de la respuesta en frecuencia ideal
kc = int(len(n)*fc)
print(kc)

Hd = np.zeros_like(n, dtype=np.float64); 
Hd[:kc] = 1.
Hd[len(Hd)-kc+1:] = 1.

#hd = 2*fc*np.sinc(2*fc*n/Fs)/Fs  #pasa bajo 
hd = 1-2*fc*np.sinc(2*fc*n/Fs)/Fs  #pasa alto


#hd = (2*fc2*np.sinc(2*fc2*n/Fs)/Fs)-(2*fc*np.sinc(2*fc2*n/Fs)/Fs)

#hd = np.real(scipy.fft.ifftshift( scipy.fft.ifft(Hd)))

plt.plot(n,hd, 'r')  
 
plt.xlabel("tiempo")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 

