# Señales de Energía y Potencia


import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# INGRESO
# archivo = input('archivo de audio: ')
archivo = 'Alarm01.wav'
#archivo = 'mysinewave.wav'

# PROCEDIMIENTO
muestreo, sonido = waves.read(archivo)
muestra = len(sonido)
dt = 1/muestreo
t = np.arange(0,muestra*dt,dt)
print(muestreo)
print(sonido)

uncanal = sonido[:,0]
#print(uncanal)

# SALIDA - Observación intermedia
plt.plot(t,uncanal)
plt.xlabel('t segundos')
plt.ylabel('sonido(t)')
plt.show()