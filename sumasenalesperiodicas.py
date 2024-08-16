import numpy as np
import matplotlib.pyplot as plt
import csv

f1=25
f2=50
T=1/10

t = np.linspace(T,1,num=100*f2)

print(t)
print(type(t))
print(t.size)              

s2=1*np.sin(2*np.pi*f1*t)
s3=1*np.sin(2*np.pi*f2*t)
s1=s2+s3
print(s1)
print(s1.size)

#f=np.savetxt("tiempo.csv",t,fmt='%6f')

g=np.savetxt("voltaje.csv",s1,fmt='%6f')




plt.figure()
# graficamos la serie Voltaje1
#plt.plot(t, s2, color='blue', linewidth=1, linestyle='dashed', label='Medición 1')
#plt.plot(t, s3,color='red', linewidth=1, linestyle='dashed', label='Medición 1')
plt.plot(t, s1,color='red', linewidth=1,  label='voltaje')


plt.show() 