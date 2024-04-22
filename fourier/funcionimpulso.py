import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as sig


D=sig.unit_impulse(12)
Tmax=8
Fs=1
print(D)
"""
n = np.arange(0,Tmax, 1/Fs)

plt.stem(n,D )  


plt.grid()
plt.show() 
"""