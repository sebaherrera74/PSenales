#Analisis en frecuencia de una señal de audio
# Incluir librerías
from scipy import signal
from scipy import fft
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


filename = './fourier/bajo'                       # nombre de archivo
fs, data = wavfile.read(f'{filename}.wav') # frecuencia de muestreo y datos de la señal

#-----------Definición de parámetros temporales:

ts = 1 / fs                             # tiempo de muestreo
N = len(data)                           # número de muestras en el archivo de audio
t = np.linspace(0, N * ts, N)           # vector de tiempo

if len(data.shape) > 1:
    senial = data[:, 0]                 # Si el audio es estereo, se extrae un canal de la pista
else:
    senial = data
#senial = senial * 3300.0 / (2 ** 16 - 1)# se escala la señal a mV (considerando un CAD de 16bits y Vref 3.3V)




freq = fft.fftfreq(N, d=1/fs)   # se genera el vector de frecuencias
senial_fft = fft.fft(senial)    # se calcula la transformada rápida de Fourier

# El espectro es simétrico, nos quedamos solo con el semieje positivo
f = freq[np.where(freq >= 0)]
#senial_fft = senial_fft[np.where(freq >= 0)]

# Se calcula la magnitud del espectro
senial_fft_mod = np.abs(senial_fft) / N     # Respetando la relación de Parceval
# Al haberse descartado la mitad del espectro, para conservar la energía
# original de la señal, se debe multiplicar la mitad restante por dos (excepto
# en 0 y fm/2)
#senial_fft_mod[1:len(senial_fft_mod-1)] = 2 * senial_fft_mod[1:len(senial_fft_mod-1)]


# Se crea una gráfica que contendrá dos sub-gráficos ordenados en una fila y dos columnas
fig1, ax1 = plt.subplots(1, 2, figsize=(20, 10))
fig1.suptitle(filename, fontsize=18)

#Grafica de la señal temporal y del espectro en frecuencias
# Se grafica la señal temporal
ax1[0].plot(t, senial)
ax1[0].set_xlabel('Tiempo [s]', fontsize=15)
ax1[0].set_ylabel('Tensión [V]', fontsize=15)
ax1[0].set_title('Señal temporal', fontsize=15)
ax1[0].set_xlim([0, ts*N])
ax1[0].grid()

# se grafica la magnitud de la respuesta en frecuencia
ax1[1].plot(freq, senial_fft_mod)
ax1[1].set_xlabel('Frecuencia [Hz]', fontsize=15)
ax1[1].set_ylabel('Magnitud [V]', fontsize=15)
ax1[1].set_title('Magnitud de la Respuesta en Frecuencia', fontsize=15)
ax1[1].set_xlim([-5000, 5000])
ax1[1].grid()

plt.show()


#Implementacion de un filtro

"""
#IIR
s = 360

# Se analiza el orden necesario para cumplir los requisitos utilizando un filtro Butterworth
N, wn = signal.buttord([5, 15], [1, 50], 3, 20, analog=False, fs=fs)
# Se genera el filtro con el orden calculado
sos_iir_3 = signal.butter(N, wn, 'bandpass', analog=False, output='sos', fs=fs)

print("Secciones de orden 2:")
print(sos_iir_3)
"""

#FIR
# Proponemos un orden
N = 2001
num_fir_3 = signal.firwin(N, cutoff=1000, window='hamming', pass_zero='lowpass', fs=fs)

#print("Coeficientes del filtro:")
#print(num_fir_3)

# se genera un vector de frecuencias
f = np.logspace(-1, 3, int(1e3))
# se analiza la respuesta en frecuencia de ambos filtros
#f, h_iir_3 = signal.sosfreqz(sos_iir_3, worN=f, fs=fs)
f, h_fir_3 = signal.freqz(num_fir_3, 1, worN=f, fs=fs)

# se grafican ambas respuestas en frecuencia superpuestas
fig1, ax1 = plt.subplots(1, 1, figsize=(10, 7), sharex=True)
ax1.plot(f, 20*np.log10(abs(h_fir_3)), label='Filtro FIR')
ax1.set_ylabel('Ganancia [dB]', fontsize=15)
ax1.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax1.grid(which='both')
ax1.legend(loc="lower right", fontsize=15)
ax1.set_title('Filtro IIR vs FIR', fontsize=15)
ax1.set_xscale('log')
ax1.set_xlim([1, 10000])
ax1.set_ylim([-80, 10])
plt.show()



#Aplico señal al filtro propuesto y se obtiene la señal filtrada

senial_fir = signal.lfilter(num_fir_3, 1, senial)


ts = 1 / fs                             # tiempo de muestreo
N = len(senial_fir)   


# graficación de las señales Original y filtrada 
fig1, ax1 = plt.subplots(1, 1, figsize=(15, 10), sharex=True)


ax1.plot(t, senial, label='Señal original')
ax1.plot(t, senial_fir, label='Señal filtrada FIR', color='g')
ax1.set_ylabel('Amplitud [mV]', fontsize=12)
ax1.set_xlabel('Tiempo [s]', fontsize=12)
ax1.legend(loc="upper right", fontsize=12)
ax1.set_title('Filtro FIR', fontsize=15)
ax1.set_xlim([0, ts*N])
#ax1.set_ylim([-1, 1.5])
ax1.grid()

plt.show()



#Grafica del Espectro 
freq = fft.fftfreq(N, d=1/fs)   # se genera el vector de frecuencias
senial_fft = fft.fft(senial_fir)    # se calcula la transformada rápida de Fourier

# El espectro es simétrico, nos quedamos solo con el semieje positivo
f = freq[np.where(freq >= 0)]
#senial_fft = senial_fft[np.where(freq >= 0)]

# Se calcula la magnitud del espectro
senial_fft_mod = np.abs(senial_fft) / N     


fig1, ax1 = plt.subplots(1, 2, figsize=(20, 10))
fig1.suptitle(filename, fontsize=18)

#Grafica de la señal temporal y del espectro en frecuencias
# Se grafica la señal temporal
ax1[0].plot(t, senial_fir)
ax1[0].set_xlabel('Tiempo [s]', fontsize=15)
ax1[0].set_ylabel('Tensión [V]', fontsize=15)
ax1[0].set_title('Señal temporal', fontsize=15)
ax1[0].set_xlim([0, ts*N])
ax1[0].grid()

# se grafica la magnitud de la respuesta en frecuencia
ax1[1].plot(freq, senial_fft_mod)
ax1[1].set_xlabel('Frecuencia [Hz]', fontsize=15)
ax1[1].set_ylabel('Magnitud [V]', fontsize=15)
ax1[1].set_title('Magnitud de la Respuesta en Frecuencia', fontsize=15)
ax1[1].set_xlim([-5000, 5000])
ax1[1].grid()

plt.show()




"""
# Se calcula el espectro en potencia
senial_fft_pot = np.power(senial_fft_mod , 2)


# Se detecta la posición de los picos en la FFT
armonicos,_= signal.find_peaks(senial_fft_pot
                               ,
                                 distance=10*N/fs,
                                 prominence=np.max(senial_fft_pot)/50)

print(armonicos)
print(len(armonicos))

print(f"La frecuencia fundamental del tono es de:")
print(f"  f0: {f[armonicos[0]]:.2f}Hz")

print("La frecuencia fundamental de los primeros 5 armónicos es de:")
for i in range(1, len(armonicos)):
    print(f"  f{i}: {f[armonicos[i]]:.2f}Hz")
    if i == 5:
        break
"""
