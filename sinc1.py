import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft

f = np.arange(-2, 2, step=1e-2)

Ts = 2
S = Ts*np.sinc(f*Ts)

plt.figure(figsize=(15,5))
plt.plot(f,S, 'r')  

plt.xlabel("tiempo")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show() 


