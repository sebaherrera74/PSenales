import numpy as np
import matplotlib.pyplot as plt
f0 = 1.23 
T = 5 
Fs = 2.23

t_c = np.arange(0, T, step=1e-4)
t_d = np.arange(0, T, step=1/Fs)
s_c = np.cos(2.0*np.pi*f0*t_c)
s_d = np.cos(2.0*np.pi*f0*t_d)
s_a = np.cos(2.0*np.pi*(Fs-f0)*t_c)





# Gráficas
plt.plot(t_c, s_c)
plt.stem(t_d, s_d)
plt.plot(t_c, s_a)

plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.show()