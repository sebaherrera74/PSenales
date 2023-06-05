import numpy as np
import matplotlib.pyplot as plt
#a)
#  w0*t=5*t    w0=5 2*pi*f0=5  f0=5/(2*pi)


f1=5/(2*np.pi)
#b)
#f1=30/105
#c)
#f1=3
#d)
#f1=3/2*np.pi #No es periodica
#e)
#f1=62/10


#fs=100

t=np.arange(0,20,0.5)
print(t)
#a)
senal1=3*np.cos(f1*t+(np.pi/6))
#senal1=np.cos(2*np.pi*f1*t+(np.pi))

señal1=np.cos((np.pi/2)*n))
señal2
señal3=....
resultante=señal1-señal2+señal3


plt.figure(figsize=(15,5))
plt.stem(t,senal1, 'b')  #, label="señal 1 f=1 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()