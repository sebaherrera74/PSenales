# Señales continuas

import numpy as np
import matplotlib.pyplot as plt
import time 
t0 = 0
tn = 200
n = 1000

# PROCEDIMIENTO
# vector de tiempo
dt = (tn-t0)/n
ti = np.arange(t0,tn,dt)

f=10
T=1/f

t = np.linspace(T,1000)
diff=t[1]-t[0]

#s1=t*1.5

#Suma de 2 señales que da una señal aperiodica
#s2=0.9*np.sin(np.pi*t)
#s3=0.9*np.sin(3*t)
#1) 0.07142*sin(0.2375*t+0.8141)
#2) 0.05027*sin(0.301*t-0.5351)
#3) 0.04565*sin(0.5876*t+0.7445)
#Suma de 2 señales que da una señal periodica
s2=0.07142*np.sin(0.2375*ti+0.8141)
s3=0.05027*np.sin(0.301*ti-0.5351)
s4=0.04565*np.sin(0.5876*ti+0.7445)
s5=0.1651*np.sin(0.2379*ti+0.7281)
s6= 0.03147*np.sin(0.06512*ti-1.109)
#Suma de señales diferentes amplitud igual periodo
#s2=1*np.sin(np.pi*t)
#s3=2*np.sin(np.pi*t)
s1=s3+s2+s4+s5+s6
fig, ax = plt.subplots()
ax.plot(ti,s1)#t)#,s2,t,s3)
plt.show()

 
