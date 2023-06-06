'''Leer un acrhivo .csv, onda seno del orden de los 18 Khz '''

import numpy as np 
import matplotlib.pyplot as plt

#from scipy.fft import fft, fftfreq

filename = './mediciones/medsenoHz.csv'
raw_data = open(filename)
print(raw_data)
data = np.loadtxt(raw_data, delimiter=",",skiprows=11)
print(type (data))
#print(data)


print(data.shape)
fila,columna=data.shape
print(fila,columna)
print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x=data[0:10000,0]
#x=x*2e-8
print(x)
#print(data[0:10000,1])
y=data[0:10000,1]
print(y)

plt.title('Mediciones En onda seno')
plt.xlabel('Muestras')
plt.ylabel('MiliVolts')
plt.plot(x,y)
plt.show()

'''
N = 600
# sample spacing
T = 1.0 / 800.0

yf = fft(y)
xf = fftfreq(N, T)[:N//2]

plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.show()
'''