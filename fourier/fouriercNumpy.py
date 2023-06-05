import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft

# Tasa de sampleo
sr = 2000
# Intervalo de sampleo
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitud')
plt.title(" Funcion Senoidal")

plt.show()


X = fft(x)
N = len(X)
print(N)
n = np.arange(N)
print(n)
T = N/sr
freq = n/T 
print(freq)
print(X)
print(np.abs(X))
plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b',markerfmt=" ", basefmt="-b")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('FFT Amplitud |X(freq)|')
plt.xlim(-10, 10)
plt.title(" Respuesta en frecuencia de Funcion Senoidal")

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title(" Funcion reconstruida")
plt.tight_layout()
plt.show()