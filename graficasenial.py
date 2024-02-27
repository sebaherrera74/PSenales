import numpy as np 
import matplotlib.pyplot as plt

from scipy.fft import fft, fftfreq

#sistema lineal 
def lineal_system(x):
    return np.array([0.5*(-1.0*item) for item in x])


f=10 
tmin=0.0
tmax=1
t=np.linspace(tmin,tmax,400)

x_1=np.sin(2*np.pi*f*t)
y_1=lineal_system(x_1)

print(x_1)
print(y_1)
plt.plot(t,x_1)
plt.plot(t,y_1)
plt.show()

