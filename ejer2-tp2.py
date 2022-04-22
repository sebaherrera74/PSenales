import numpy as np
import matplotlib.pyplot as plt
#a)
#f1=0.01
#b)
#f1=30/105
#c)
#f1=3
#d)
#f1=3/2*np.pi #No es periodica
#e)
f1=62/10

fs=100
t=np.arange(0,4,0.01)
print(t)

senal1=np.cos(f1*np.pi*t)


plt.figure(figsize=(15,5))
plt.plot(t,senal1, 'b')  #, label="señal 1 f=1 Hz")
#plt.plot(t,senal2, 'r', label="señal 2 f=11 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()