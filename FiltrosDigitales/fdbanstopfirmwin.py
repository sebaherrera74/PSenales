import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as sig



fc1 =100 # Frecuencia de corte1
fc2=500   #Frecuencia de corte 2 
Fs =5000 # Frecuencia de muestreo
L = 1000+1 # Largo del filtro


N=512

h = sig.firwin(L, (fc1,fc2), window='hamming', pass_zero='bandstop', fs=Fs)
freq, H = sig.freqz(h, fs=Fs)



#Probemos si filtra 

# señal en el tiempo $
Tmax=4
t = np.arange(0,Tmax, 1/Fs)
x = np.sin(2*np.pi*300*t)+np.sin(2*np.pi*450*t)+np.cos(2*np.pi*1000*t)  #Probar cambiando la frecuenciamas alta
X = np.fft.fft(x,N)
# salida del filtro
y=np.convolve(x,h)
Y = np.fft.fft(y,N)

#Graficas  

fig1,axs1 = plt.subplots(4,1)
fig1.set_size_inches((15,16))
plt.subplots_adjust(hspace=0.3)


# Respuesta al impulso
ax=axs1[0]
ax.plot(range(len(h)), h)
ax.set_xlabel("$frec$",fontsize=12)
ax.set_ylabel("$hi[w]$",fontsize=12)

# Respuesta en frecuencia del filtro
ax=axs1[1]
ax.plot(freq, np.absolute(H))
ax.set_xlabel("$Frec$",fontsize=12)
ax.set_ylabel("$h[w]$",fontsize=12)

# Señal de Entrada  
ax=axs1[2]
ax.plot(x[0:1000], label="señal de entrada")
ax.set_xlabel("$n$",fontsize=12)
ax.set_ylabel("$x[n]$",fontsize=12)

#Señal de salida
ax=axs1[3]
ax.plot(y[0:2000], label="señal de salida")
ax.set_xlabel("$n$",fontsize=12)
ax.set_ylabel("$y[n]$",fontsize=12)

plt.legend()
plt.grid()
plt.show() 
