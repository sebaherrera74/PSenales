# Señales continuas

import numpy as np
import matplotlib.pyplot as plt
import time 
f=10
T=1/f

t = np.linspace(T,400)
diff=t[1]-t[0]

#s1=t*1.5

#Suma de 2 señales que da una señal aperiodica
s2=0.9*np.sin(np.pi*t)
s3=0.9*np.sin(3*t)

#Suma de 2 señales que da una señal periodica
#s2=0.9*np.sin(np.pi*t)
#s3=0.3*np.sin(3*np.pi*t)


#Suma de señales diferentes amplitud igual periodo
#s2=1*np.sin(np.pi*t)
#s3=2*np.sin(np.pi*t)
s1=s2+s3
fig, ax = plt.subplots()
ax.plot(t,s1,t,s2,t,s3)
plt.show()

''' 
if __name__ == '__main__':
    while True:
        t=np.delete(t,0)
        t=np.append(t,t[-1]+diff)
        s1=t*1.5
        s2=1*np.sin(2*t*np.pi*f)
        s3=2*np.sin(2*t*np.pi*6*f)
        s1=s2+s3
        plt.cla()
        ax.plot(t,s1,'b',t,s2,'b',t,s3,'g')
        plt.pause(0.02)
    plt.show()  '''