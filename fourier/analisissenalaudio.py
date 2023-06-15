#Analisis temporal de una señal de audio 
# Incluir librerías
from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

filename = './fourier/silbido'                       # nombre de archivo
fs, data = wavfile.read(f'{filename}.wav') # frecuencia de muestreo y datos de la señal

print(fs)
#print(data)

ts = 1 / fs                             # tiempo de muestreo
N = len(data)                           # número de muestras en el archivo de audio
#print(N)

t = np.linspace(0, N * ts, N)           # vector de tiempo
#print(t)


if len(data.shape) > 1:
    senial = data[:, 0]                 # Si el audio es estereo, se extrae un canal de la pista 
else:
    senial = data   

#print (senial)

senial = senial * 3300.0 / (2 ** 16 - 1)# se escala la señal a mV (considerando un CAD de 16bits y Vref 3.3V)


# Se crea una gráfica 
fig1, ax1 = plt.subplots(1, 1, figsize=(20, 10))
fig1.suptitle("Acorde", fontsize=18)

# Se grafica la señal
ax1.plot(t, senial, label='Señal de audio', color='blue')
ax1.set_xlabel('Tiempo [s]', fontsize=15)
ax1.set_ylabel('Tensión [mV]', fontsize=15)
ax1.set_xlim([0, ts*N])
ax1.grid()
ax1.legend(fontsize=12)
plt.show()

# --------------------Cálculo de parámetros temporales

# --------------------Valor medio
mean_value = np.mean(senial)

print(f"El valor medio de la señal es de {mean_value:.5f}mV")

#---------------------Máximo

max = np.max(senial)

print(f"El máximo de la señal es de {max:.5f}mV")

#---------------------Minimo

min = np.min(senial)

print(f"El mínimo de la señal es de {min:.5f}mV")

#---------------------Máximo absoluto

abs_max = np.max(np.abs(senial))

print(f"El máximo absoluto de la señal es de {abs_max:.5f}mV")

#---------------------------Mínimo absoluto

abs_min = np.min(np.abs(senial))

print(f"El mínimo absoluto de la señal es de {abs_min:.5f}mV")


#------------------------Muestras por encima de la media
above_mean = np.count_nonzero(np.where(senial>mean_value, True, False))

print(f"La cantidad de muestras por encima de la media es de {above_mean}")

#---------------Muestras por debajo de la media

below_mean = np.count_nonzero(np.where(senial<mean_value, True, False))

print(f"La cantidad de muestras por debajo de la media es de {below_mean}")


#---------------------Valor eficaz (RMS)

rms = np.sqrt(np.mean(np.power((senial-mean_value), 2)))

print(f"El valor eficaz es de {rms:.5f}mV")
