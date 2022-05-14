import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as win

f0=2.15
Fs=20
T= 2
t = np.arange(-T, T, step=1/Fs)
sT = np.cos(2*np.pi*f0*t)
f_os = sfft.rfftfreq(n=len(t)*10, d=1/Fs)
rect = lambda N: np.ones(shape=(N,))

#[rect, tukey, cosine, blackman]:
w = win.hamming(len(sT))            #Cambiar Tukey,cosine,blackman
ST_os = np.absolute(sfft.rfft(sT*w, n=len(sT)*10))    

#Graficas de las diferentes ventanas 
plt.figure(figsize=(15,5))
plt.plot(f_os,ST_os, 'r')  
plt.xlabel("frecuencia")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 
