"""Programa que me permite abrir un archivo .txt creado en LTSPICE 
Aqui estoy abriendo las simulaciones en base a diferentes tensiones de Drain

Graficar usando subplot 
"""

import numpy as np 
import matplotlib.pyplot as plt


from scipy.fft import fft, fftfreq

filename = "./setoscvd25mv.txt"
filename1 = "./setoscvd30mv.txt"
filename2 = "./setoscvd35mv.txt"
filename3 = "./setoscvd40mv.txt"
raw_data = open(filename)
raw_data1 = open(filename1)
raw_data2 = open(filename2)
raw_data3 = open(filename3)
#print(raw_data)
data = np.loadtxt(raw_data,skiprows=0)
data1 = np.loadtxt(raw_data1,skiprows=0)
data2 = np.loadtxt(raw_data2,skiprows=0)
data3 = np.loadtxt(raw_data3,skiprows=0)


#print(data)
#print(data.shape)
fila,columna=data.shape
#print(fila,columna)
#print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x=data[0:10000,0]
#print(x)
#print(data[0:20000,1])
y=data[0:10000,1]
Maximo=np.max(y)
print("El valor maximo es :" ,Maximo)

fila1,columna1=data1.shape
#print(fila,columna)
#print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x1=data1[0:10000,0]
#print(x)
#print(data[0:20000,1])
y1=data1[0:10000,1]
Maximo1=np.max(y1)
print("El valor maximo es :" ,Maximo1)

fila2,columna2=data2.shape
#print(fila,columna)
#print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x2=data2[0:10000,0]
#print(x)
#print(data[0:20000,1])
y2=data2[0:10000,1]
Maximo2=np.max(y2)
print("El valor maximo es :" ,Maximo2)

fila3,columna3=data3.shape
#print(fila,columna)
#print(data.size)
#print(data[1:2])
#print(data[0:10000,0])
x3=data3[0:10000,0]
#print(x)
#print(data[0:20000,1])
y3=data3[0:10000,1]
Maximo3=np.max(y3)
print("El valor maximo es :" ,Maximo3)

vd=np.arange(25,45,5)
print(vd)

MaximmosV=np.array([Maximo,Maximo1,Maximo2,Maximo3])
print(MaximmosV)


fig,ax=plt.subplots(2,2)






ax[0,0].title.set_text("Tension Vdrain=25mv")
ax[0,0].set_xlabel("Time (s)",size=8)
ax[0,0].set_ylabel("Voltage (volts)", size=8)

ax[0,0].plot(x,y)


ax[0, 1].title.set_text("Tension Vdrain=30mv")
ax[0,1].set_xlabel("Time (s)",size=8)
ax[0,1].set_ylabel("Voltage", size=8)

ax[1,0].plot(x1,y1)
ax[1, 0].title.set_text("Tension Vdrain=35mv")
ax[0,1].plot(x2,y2)
ax[1, 1].title.set_text("Tension Vdrain=40mv")
ax[1,1].plot(x3,y3)
#titulo=ax.set_title("Prueba")

plt.show()


"""
plt.title('Simulaciones en SET Vdrain=25mVolts ')
plt.xlabel('tiempo')
plt.ylabel('Volts')
plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)


plt.show()

plt.plot(vd,MaximmosV)
plt.show()
"""