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


