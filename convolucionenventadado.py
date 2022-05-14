import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft


T = 5 # Duración de la ventana
Fs = 20 # Frecuencia de muestre
f0 = 1.2345 # Frecuencia fundamental
t = np.arange(-6, 6, step=1/Fs)
s = np.cos(2*np.pi*f0*t)
w = np.zeros_like(t)
w[np.absolute(t) < T/2] = 1
sT = s*w

plt.figure(figsize=(15,5))
plt.plot(t,sT, 'r')  
plt.xlabel("tiempo")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 