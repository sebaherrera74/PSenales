import numpy as np
import matplotlib.pyplot as plt
f1=1.0
f2=11.0



fs=100
t=np.arange(0,2,1/fs)
print(t)

senal1=np.sin(2*np.pi*f1*t)
senal2=np.sin(2*np.pi*f2*t)

plt.figure(figsize=(15,5))
plt.plot(t,senal1, 'b', label="señal 1 f=1 Hz")
plt.plot(t,senal2, 'r', label="señal 2 f=11 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show()