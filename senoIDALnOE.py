# Señales continuas

import numpy as np
import matplotlib.pyplot as plt


#1) 0.07142*sin(0.2375*t+0.8141)


# INGRESO parámetros
A=0.07142
fase=0.8141

#frecuencia=39
w  = 0.2375 #2*np.pi*frecuencia
fx = lambda t: A*np.sin(w*t+fase)

#2) 0.05027*sin(0.301*t-0.5351)
# INGRESO parámetros
A1=0.05027
fase1=0.5351


w1  = 0.301#2*np.pi*frecuencia
fx1 = lambda t: A1*np.sin(w1*t+fase1)
ftotal=fx+fx1


t0 = 0
tn = 200
n = 1000

# PROCEDIMIENTO
# vector de tiempo
dt = (tn-t0)/n
ti = np.arange(t0,tn,dt)




# señal
senal = ftotal(ti)


# SALIDA

np.set_printoptions(precision = 4)
print('tiempo: ')
print(ti)
print('señal: x(t) ')
print(senal)

# Gráfica
plt.plot(ti,senal)
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('t')
plt.ylabel('señal x[(t)]')
plt.show()
