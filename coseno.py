# Se analiza una señal coseno(), con periodo T=2π, en un rango de dos 
# periodos m=2, y 50 muestras, luego se determina el vector t para el 
# rango de observación y se calcula la señal


import matplotlib.pyplot as plt
import numpy as np

# ingresar parametros
T = 2*np.pi
f = 1/T
w = 2*np.pi*f
fx = lambda t:np.cos(w*t)
m  = 2 #periodos para la grafica
t0 = 0
n  = 50

# PROCEDIMIENTO
# vector de tiempo
tn=T*m
dt=(tn-t0)/n
ti=np.arange(t0,tn,dt)

# señal
senal=fx(ti)

# marcar un periodo en [desde, hasta)
desde=T/4
hasta=desde + T + dt
tperiodo=np.arange(desde,hasta,dt)
periodo=fx(tperiodo)

# SALIDA
# Grafica
plt.plot(ti,senal)
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('t')
plt.ylabel('señal x[(t)]')

# marcar un periodo
plt.title('marcando un periodo')
plt.fill_between(tperiodo,0, periodo,facecolor='green')
plt.show()