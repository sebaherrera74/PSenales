# Señales- Operaciones


import numpy as np
import matplotlib.pyplot as plt

Fs = 100000           #[Hz ]Sampling frequency                    
T = 1/Fs              #[s] Sampling period       
L = 20000             #[samples] Length of signal
t = np.array(range(0,L))*T         #[s] Time vector
MaxT = L/Fs           #[s] Tiempo maximo

A1 = 5                #[V] amplitud
A2 = 4                #[V] amplitud
FREC1= 200            #[Hz] Frecuencia de la señal y la referencia
OMEGA1 = 2*np.pi*FREC1    #[rad/s] frecuencia angular
FREC2= 50            #[Hz] Frecuencia de la señal y la referencia
OMEGA2 = FREC2*2*np.pi     #[rad/s] frecuencia angular
FASE1 =10       #[rad] Fase de la señal respecto a la referencia
FASE2 =0 #np.pi/2      #[rad] Fase de la señal respecto a la referencia
ruido = 4             #[V] ruido


#Armo la señal con dos tramos de distinta amplitud y fase, y le sumo ruido
k=2
S1=A1*np.sin(OMEGA1*t+FASE1)

#S11=A1*np.sin(OMEGA1*t*k)
#S12=A1*np.sin(OMEGA1*(-t))
S2=A2*np.sin(np.pi*OMEGA2*t+FASE2)
plt.clf()
S3=S1+S2
plt.plot(t,S3)
#plt.plot(t,S2)

#plt.plot(t,S3)
plt.show()


#plt.plot(t,senial)




#plt.plot(t,SENIAL)
#plt.show()
#RUIDO = ruido*np.random.randn(len(SENIAL));
#ORIGINAL = SENIAL + RUIDO;





