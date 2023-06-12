"""Ejemplo de señales de audio con fourier """

# Example 1: FFT of a DFT-sinusoid

import numpy as np
from numpy import pi, cos, log10
from numpy.fft import fft
import matplotlib.pyplot as plt

# Parameters:
N = 64              # debe ser potencia de 2
T = 1               # Seteo tasa de sampleo a 1
A = 1               # Amplitud sinusoidal 
phi = 0             # Fase de la sinusoidal 
f = 0.25            # Frecuencia (cycles/sample)
n = np.arange(N)          # Eje del tiempo discreto
x = A*cos(2*pi*n*f*T+phi) # Ecuacion Sinusoidal 
X = fft(x)                # Calculo del espectro 

#print(X)
#print(abs(X))

plt.figure(figsize=(10,10))

# Plot time data:
plt.subplot(3,1,1)
plt.plot(n,x,'*k')        
ni = np.arange(0,N,0.1)   # Eje del tiempo Interpolado 
plt.plot(ni,A*cos(2*pi*ni*f*T+phi),'-k') 
plt.xlim(0,N)
plt.title('Sinusoide a 1/4 de la tasa de muestreo')
plt.xlabel('Time (samples)') 
plt.ylabel('Amplitude')
plt.text(-.11*64,1,'a)')


# Plot spectral magnitude:
magX = abs(X)
fn = np.arange(0, 1, 1/N)  # Normalized frequency axis
plt.subplot(3,1,2)
plt.stem(fn,magX,'-ok', use_line_collection=True)
plt.grid()
plt.xlim(0,1)
plt.xlabel('Normalized Frequency (cycles per sample))') 
plt.ylabel('Magnitude (Linear)')
plt.text(-.11,30,'b)')

# Same thing on a dB scale:
spec = 20*log10(magX) # Spectral magnitude in dB
plt.subplot(3,1,3)
plt.plot(fn,spec,'--ok')
plt.grid()
plt.xlim(0,1)
plt.ylim(-350, 50)
#plt.axis([0 1 -350 50])
plt.xlabel('Normalized Frequency (cycles per sample))') 
plt.ylabel('Magnitude (dB)')
plt.text(-.11,0,'c)')

plt.show()

