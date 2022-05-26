import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as sig

'''
Ejemplo de un filto pasabajo sin enventanado, y su respuesta al impulso


'''

wc = np.pi/4
M=20
N = 512 # DFT size
n = np.arange(-M,M)
h = wc/np.pi * np.sinc(wc*(n)/np.pi)  # see definition of np.sinc()

w,Hh = sig.freqz(h,1,whole=True, worN=N) #obtener el dominio de frecuencia completo
wx = sfft.fftfreq(len(w)) #Cambia el centro para la traza

fig,axs = plt.subplots(3,1)    #Me devuelve el tamaño de una imagen(fig) y la cantidad de graficas que quiero
print (fig)
print(axs)
fig.set_size_inches((8,8))
plt.subplots_adjust(hspace=0.3)

#Grafica de una Sinc aplicada respuesta a un filtro pasa bajo
#Esto es en el tiempo de muestras 
ax=axs[0]
ax.stem(n+M,h,basefmt='b-')
ax.set_xlabel("n",fontsize=16)
ax.set_ylabel("amplitude",fontsize=16)

#Grafica la respuesta en frecuencia del filtro pasa bajo 
ax=axs[1]
ax.plot(w-np.pi,abs(sfft.fftshift(Hh)))
ax.axis(xmax=np.pi/2,xmin=-np.pi/2)
ax.vlines([-wc,wc],0,1.2,color='g',lw=2.,linestyle='--',)
ax.hlines(1,-np.pi,np.pi,color='g',lw=2.,linestyle='--',)
ax.set_xlabel(r"$\omega$",fontsize=22)
ax.set_ylabel(r"$|H(\omega)| $",fontsize=22)
ax.grid()

#Grafica la respuesta en frecuencia del filtro pasa bajo 
#en escala logaritmica
ax=axs[2]
ax.plot(w-np.pi,20*np.log10(abs(sfft.fftshift(Hh))))
ax.axis(ymin=-40,xmax=np.pi/2,xmin=-np.pi/2)
ax.vlines([-wc,wc],10,-40,color='g',lw=2.,linestyle='--',)
ax.hlines(0,-np.pi,np.pi,color='g',lw=2.,linestyle='--',)
ax.grid()
ax.set_xlabel(r"$\omega$",fontsize=22)
ax.set_ylabel(r"$20\log_{10}|H(\omega)| $",fontsize=18)


plt.grid()
plt.show() 
