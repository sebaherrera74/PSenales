import numpy as np
import matplotlib.pyplot as plt
import csv
#programa para sumar señales senoidles de diferentes frecuencias
#y cargarlo en el generador de funciones



f1=3900
f2=90000
T=1

t = np.linspace(0,T,num=1000*f2)

print(t)
print(type(t))
print(t.size)              

s2=np.sin(2*np.pi*f1*t)
s3=np.sin(2*np.pi*f2*t)
s1=s2+s3
print(s1)
print(s1.size)

#f=np.savetxt("tiempo.csv",t,fmt='%6f')

g=np.savetxt("voltaje2.csv",s1,fmt='%6f')




plt.figure()
# graficamos la serie Voltaje1
#plt.plot(t, s2, color='blue', linewidth=1, linestyle='dashed', label='Medición 1')
#plt.plot(t, s3,color='red', linewidth=1, linestyle='dashed', label='Medición 1')
plt.plot(t, s1,color='red', linewidth=1,  label='voltaje')


@