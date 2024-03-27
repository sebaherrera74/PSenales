import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.fft import fft, fftfreq

filename = "senalesSistemas/vds1.txt"

raw_data=open(filename)

print(raw_data)
data=np.loadtxt(raw_data,skiprows=0)



#print(data)
#print(data.shape)
fila,columna=data.shape
#print(fila,columna)
#print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x=data[0:10,0]
#print(x)
#print(data[0:20000,1])
y=data[0:10,1]
Maximo=np.max(y)
print("El valor maximo es :" ,Maximo)






vd=np.arange(25,45,5)
print(vd)

MaximmosV=np.array([Maximo])
print(MaximmosV)

plt.title('Simulaciones en SET Vdrain=25mVolts ')
plt.xlabel('volts')
plt.ylabel('corriente')
plt.plot(y,x)



plt.show()


spline = InterpolatedUnivariateSpline(x, y)

x_new = np.linspace(0,10,10)
print(x_new)
y_new = spline(x_new)
print(y_new)

plt.plot(x,y)
plt.plot(x_new,y_new)
plt.show()
