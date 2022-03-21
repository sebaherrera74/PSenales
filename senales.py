import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

# INGRESO
# archivo = input('archivo de audio: ')
archivo = 'Alarm01.wav'
muestreo, sonido = waves.read(archivo)

# SALIDA - Observacion intermedia
print('frecuencia de muestreo: ', muestreo)
print('dimensiones de matriz: ', np.shape(sonido))
print('datos de sonido: ')
print(sonido)

# Fragmento de tiempo
inicia = 2600
termina = 2720
canal = 0

# Extrae el fragmento de sonido
dt = 1/muestreo
t = np.arange(inicia*dt,termina*dt,dt)
muestras = len(t)
fragmento = sonido[inicia:inicia+muestras, canal]

#SALIDA
plt.plot(t,fragmento)
plt.xlabel('t segundos')
plt.ylabel('sonido(t)')
plt.show()
