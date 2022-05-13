import numpy as np
import matplotlib.pyplot as plt
#a)#
f1=0.01
#b)
#f1=30/210
#c)
#f1=3/2
#d)
#f1=3/2*np.pi 
#e)
#f1=62/10

#-----------------------Ejercicio3
#a)
#f1=5/2*np.pi

#fs=100
n=np.arange(1,100,0.1)
print(n)


#senal1=3*np.cos(f1*n+np.pi/6)
senal1=np.cos(f1*np.pi*n)
#senal2=np.sin(f1*n)

plt.figure(figsize=(15,5))
#plt.plot(n,senal1, 'r')  #, label="señal 1 f=1 Hz")
plt.stem(n,senal1, 'r')  #, label="señal 1 f=1 Hz")
#plt.plot(t,senal2, 'r', label="señal 2 f=11 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()
