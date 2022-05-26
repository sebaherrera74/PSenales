import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft


T = 1000# Duración de la ventana, cambiar los valores de la ventana y sacar conclusiones
Fs = 100 # Frecuencia de muestreo
f0 = 1.2345 # Frecuencia fundamental
t = np.arange(0, 5, step=1/Fs)
s = np.cos(2*np.pi*f0*t)

#funcion ventana 
w = np.zeros_like(t)
w[np.absolute(t) < T/2] = 1

#print(w)


sT = s*w              #En el dominio del tiempo es solo el producto

#plt.figure(figsize=(15,5))
#plt.stem(t,w, 'r')  
#plt.plot(t,s, 'r')  
#plt.plot(t,sT, 'b')  
#plt.xlabel("tiempo")

#plt.ylabel("Amplitud")
#plt.legend()
#plt.grid()
#plt.show() 



 #Aqui saco la transformada de fourier
 # del prodcuto de s*w la señal por la ventana

freq=sfft.rfftfreq(n=len(s), d=1/Fs)

ST = np.absolute(sfft.rfft(sT)) 

plt.figure(figsize=(15,5))
plt.plot(freq,ST, 'r')  
plt.xlabel("frecuencia")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show() 
