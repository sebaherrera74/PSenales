import numpy as np 
import matplotlib.pyplot as plt

from scipy.fft import fft, fftfreq

filename = "./fig63tensiones1.txt"
raw_data = open(filename)
print(raw_data)
data = np.loadtxt(raw_data,skiprows=1)
print(data)



print(data.shape)
fila,columna=data.shape
print(fila,columna)
print(data.size)

#print(data[1:2])
#print(data[0:10000,0])
x=data[0:10000,0]

print(x)

print(data[0:20000,1])
y=data[0:10000,1]


plt.title('Simulaciones en SET')
plt.xlabel('tiempo')
plt.ylabel('Volts')
plt.plot(x,y)
plt.show()

"""
N = 600
# sample spacing
T = 1.0 / 600

yf = fft(y)

print(yf)
print(yf.size)
aux=np.abs(yf[0:N//2])
print(aux)
print(aux.size)
xf = fftfreq(N, T)[:N//2]
#print(xf)
#print(xf.size)

plt.stem(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.xlim(0, 10)
plt.show()
"""