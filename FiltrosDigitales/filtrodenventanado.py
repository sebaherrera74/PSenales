import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as sig

'''
Ejemplo de un filto pasabajo con enventanado, y su respuesta al impulso


'''

fc=1000.0 # frec de corte
fs=8000.0 # frec de muestreo
Adb=0     # Ganancia del filtro en decibeles
N = 512   # Numero de puntos de la FFT
BW=200    # Ancho de banda en la banda de transicion



# 1. frecuencia de corte normalizada en radianes
wc = 2*np.pi*fc/fs  

# 2. ancho de banda  normalizado en radianes
bwn=2*np.pi*BW/fs                      

# 3. orden estimado del filtro
M=int(4/bwn)                           
print('El orden del filtro es: ', M)

# 4. Respuesta del filtro ideal h1[n]
n = np.arange(-M,M)
h1 = wc/np.pi * np.sinc(wc*(n)/np.pi) # filtro pasabajas, recuerde cambiar cuando pasaaltas, pasabanda, o rechazabanda
w1,Hh1 = sig.freqz(h1,1,whole=True, worN=N) # Respuesta en frecuencia del filtro ideal

# 5. Truncamiento de frecuencia en el origen h1[0]

#h1[n==0]=1-(wc)/np.pi # cuando es pasa--altas
#h1[n==0]=(wc2-wc1)/np.pi # cuando es pasabanda
#h1[n==0]=1-(wc2-wc1)/np.pi # cuando es rechazabanda

# Para el caso del filtro pasbajas no se debe aplicar

# 6. Generación de la ventana para elimnar el fenomeno de Gibbs
win= sig.hamming(len(n)) 

# 7. Multiplico la respuesta ideal por la ventana
h2=h1*win 


# 8. Ganancia del filtro
A=np.sqrt(10**(0.1*Adb))
h2=h2*A # Ganancia del filtro
w2,Hh2 = sig.freqz(h2,1,whole=True, worN=N) # Respuesta en frecuencia del filtro enventanado


u=np.ones_like(n) # escalon
un=np.convolve(u, h2, mode='full') # respuesta al escalo


fig1,axs1 = plt.subplots(5,1)
fig1.set_size_inches((15,16))
plt.subplots_adjust(hspace=0.3)

# respuesta natural 
ax=axs1[0]
ax.stem(n+M,h2,basefmt='b-')
ax.set_xlabel("$n$",fontsize=24)
ax.set_ylabel("$h_n$",fontsize=24)

ax=axs1[1]
ax.stem(n+M,h1,basefmt='b-')
ax.set_xlabel("$n$",fontsize=24)
ax.set_ylabel("$h_n$",fontsize=24)

# respuesta al escalon 
#ax=axs1[1]
#ax.stem(un,basefmt='b-')
#ax.plot(u, color='g')
#ax.set_xlabel("$n$",fontsize=24)
#ax.set_ylabel("$u_n$",fontsize=24)
#ax.axis(xmax=M*2,xmin=0)

# respuesta en frecuencia antes del enventanado 
ax=axs1[2]
ax.plot((w1-np.pi)*fs/(2*np.pi),np.abs(np.fft.fftshift(Hh1)))
ax.axis(xmax=fs/2,xmin=-fs/2)
ax.vlines([-fc,fc],0,1,color='g',lw=2.,linestyle='--')
ax.hlines(1,-fc,fc,color='g',lw=2.,linestyle='--')
ax.set_xlabel(r"$f (Hz)$",fontsize=18)
ax.set_ylabel(r"$|H1(\omega)| $",fontsize=18)

# respuesta en frecuencia despues del enventanado 
ax=axs1[3]
ax.plot((w2-np.pi)*fs/(2*np.pi),np.abs(np.fft.fftshift(Hh2)))
ax.axis(xmax=fs/2,xmin=-fs/2)
ax.vlines([-fc,fc],0,1,color='g',lw=2.,linestyle='--')
ax.hlines(1,-fc,fc,color='g',lw=2.,linestyle='--')
ax.set_xlabel(r"$f (Hz)$",fontsize=18)
ax.set_ylabel(r"$|H2(\omega)| $",fontsize=18)

ax=axs1[4]
ax.plot((w1-np.pi)*fs/(2*np.pi),np.angle(np.fft.fftshift(Hh1)))
ax.plot((w2-np.pi)*fs/(2*np.pi),np.angle(np.fft.fftshift(Hh2)))
ax.axis(xmax=fs/2,xmin=-fs/2)
ax.set_xlabel(r"$f (Hz)$",fontsize=18)
ax.set_ylabel(r"$\Theta(H(\omega)) $",fontsize=18)
ax.legend(['H1', 'H2'])

plt.grid()
plt.show() 
