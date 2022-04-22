import numpy as np
import matplotlib.pyplot as plt
#a)
f1=5/np.pi
#b)
#f1=30/105
#c)
#f1=3
#d)
#f1=3/2*np.pi #No es periodica
#e)
#f1=62/10

fs=100
t=np.arange(0,1,0.01)
print(t)
#a)
#senal1=np.cos(2*np.pi*f1*t+(np.pi/6))
senal1=np.cos(2*np.pi*f1*t+(np.pi))


plt.figure(figsize=(15,5))
plt.plot(t,senal1, 'b')  #, label="señal 1 f=1 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()