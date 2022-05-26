import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as win



f0=1
Fs=32
Ts= 1/Fs
n = np.arange(0, 40, step=2/Fs)
x_n = np.cos(2*np.pi*f0*Ts*n)

x_n_1 = np.cos(2*np.pi*f0*Ts*(n-2))     

#Forma general del filtro es y(n)=x(n)+g*x(n-r)



#y_n=x_n + x_n_1       #Filtro pasa bajo 
y_n=x_n - x_n_1       #Filtro pasa alto    


plt.figure(figsize=(15,5))

    
    
plt.plot(n,x_n, 'r')  
plt.plot(n,x_n_1, 'black')

plt.plot(n,y_n, 'b')  
plt.xlabel("tiempo")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 
