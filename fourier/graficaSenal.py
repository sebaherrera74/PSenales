import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft 
import funciones as fc


f = 10      #En Hz
f2= 20
x_1,t=fc.buildSenoidal(f,1,0)
fc.plot_time(t,x_1)
print(len(x_1))
x_2,t1=fc.buildSenoidal(f2,1,0)
print(type(x_2))
print(len(x_2))
fc.plot_time(t1,x_2)

#x_3=x_2-x_1

#fc.plot_time(t,x_3)
