import numpy as np
import matplotlib.pyplot as plt


f1=50
f2=75
T=1/10

t = np.linspace(T,1,num=100*f2)

print(t)
print(t.size)              

s2=1*np.sin(2*np.pi*f1*t)
s3=1*np.cos(2*np.pi*f2*t)
s1=s2+s3
plt.figure()
# graficamos la serie Voltaje1
#plt.plot(t, s2, color='blue', linewidth=1, linestyle='dashed', label='Medición 1')
#plt.plot(t, s3,color='red', linewidth=1, linestyle='dashed', label='Medición 1')
plt.plot(t, s1,color='red', linewidth=1, linestyle='dashed', label='Medición 1')


plt.show() 