#ejemplo de un Espectrograma 

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft 
import funciones as fc
from scipy import signal


#
f = 10 #En Hz
f2= 40
tmin = 0.0
tmax = 1.0

t   = np.linspace(tmin,tmax,800)
x_1 = np.sin(2*np.pi*f*t)
x_2 = 2*np.sin(2*np.pi*f2*t)        
print(len(x_1))
print(len(x_2))
plt.plot(t,x_1)
plt.plot(t,x_2)
plt.grid()
plt.xlabel("Tiempo[s]")
plt.ylabel("Amplitud[V]")
plt.legend(["Entrada X1","Entrada X2"])
plt.show()

rv = fc.plot_spectrum(x_1,x_2)


x_3=np.concatenate((x_1,x_2))

tmin1 = 0
tmax1 = 2.0
t1   = np.linspace(tmin1,tmax1,1600)
plt.plot(t1,x_3)

plt.grid()
plt.xlabel("Tiempo[s]")
plt.ylabel("Amplitud[V]")
plt.legend(["x_3"])
plt.show()

rv = fc.plot_spectrum(x_3,x_3)

x_4=np.concatenate((x_2,x_1))

plt.plot(t1,x_4)

plt.grid()
plt.xlabel("Tiempo[s]")
plt.ylabel("Amplitud[V]")
plt.legend(["x_4"])
plt.show()

rv1 = fc.plot_spectrum(x_4,x_4)


#Espectrograma usando scipy

N = 400 #Numero de puntos de la fft

f, t, Sxx = signal.spectrogram(x_4,fs=800,window = signal.blackman(N))#,nfft=N)
#plt.pcolormesh(t, f,10*np.log10(Sxx)) # Espectro de magnitud en dB
plt.pcolormesh(t, f,Sxx) #Espectro de Magnitud Lineal
#plt.ylim(0,150)
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [seg]')
plt.title('Espectrograma usando scipy.signal',size=16);
plt.show()

