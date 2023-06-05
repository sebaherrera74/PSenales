import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from scipy.fftpack import fft, fftfreq

n = 2**6  # Número de intervalos
print(n)
f = 400.0  # Hz
dt = 1/(f * 16)  # Espaciado, 16 puntos por período

t = np.linspace(0,(n-1)* dt, n)  # Intervalo de tiempo en segundos
y = np.sin(2*pi*f*t)-0.5*np.sin(2*pi*2*f*t)  # Señal

plt.plot(t, y)
plt.plot(t, y, 'ko')
plt.xlabel('Tiempo (s)')
plt.ylabel('$y(t)$')
plt.show()

Y = fft(y)/n          # Normalizada
frq = fftfreq(n, dt)  # Recuperamos las frecuencias
print (len(Y))
print(len(frq))
plt.plot(frq,Y.imag)
plt.show()
