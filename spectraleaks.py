import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft

Fs, T = 20, 2
t = np.arange(-T, T, step=1/Fs)
f = sfft.rfftfreq(n=len(t), d=1/Fs)
f_os = sfft.rfftfreq(n=len(t)*10, d=1/Fs)

p = []
for f0 in [2.0, 2.15]: # Frecuencia fundamental    
    sT = np.cos(2*np.pi*f0*t)    
    ST = np.absolute(sfft.rfft(sT))   
    ST_os = np.absolute(sfft.rfft(sT, n=len(sT)*10)) 
    
    
plt.figure(figsize=(15,5))
plt.plot(f,ST, 'r')  
plt.xlabel("frecuencia")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 

plt.figure(figsize=(15,5))
plt.plot(f_os,ST_os, 'r')  
plt.xlabel("frecuencia")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 
