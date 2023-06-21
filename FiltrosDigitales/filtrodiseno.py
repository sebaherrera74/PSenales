'''
Ejemplo de diseño de filtro digitales FIR e IIR
usando MIcromodeler y pyFDA
Requisitos
El filtro aplicado en el primer paso para aumentar la relación
señal-ruido consiste en un pasa-banda. Se sugiere un ancho de banda de
filtro de 5 a 15 Hz para maximizar la contribución de QRS y reducir el ruido
muscular, la desviación de la línea de base, la interferencia de la línea
eléctrica y el contenido de frecuencia de onda P/onda T.
Este filtro estaba originalmente implementado mediante un pasa bajos y
un pasa altos, y presentaba una atenuación de aproximadamente 20dB
para frecuencias de 1Hz y 50Hz.
'''


# Incluir librerías
from scipy import signal, fft
import numpy as np
import matplotlib.pyplot as plt


#------------Microdolere----------------
sos_iir_1 = [[0.023879506018041567, 0.04775901203608313, 0.023879506018041567, 1, -1.782312015127054, 0.8169043136006663],
             [0.5, -1, 0.5, 1, -1.8727120022494252, 0.8856363861548432],
             [0.0078125, 0.015625, 0.0078125, 1, -1.8452018524584375, 0.9065304015992756],
             [0.5, -1, 0.5, 1, -1.9576917383162364, 0.96562417674302]]


num_fir_1 = [-0.071488410, -0.072959286, -0.071854345, -0.062158068,
             -0.039125342, -0.0022398888, 0.043459476, 0.088364179,
             0.12130080, 0.13340178, 0.12130080, 0.088364179,
             0.043459476, -0.0022398888, -0.039125342, -0.062158068,
             -0.071854345, -0.072959286, -0.071488410]

fs = 360

# se genera un vector de frecuencias
f = np.logspace(-1, 3, int(1e3))
# se analiza la respuesta en frecuencia de ambos filtros
f, h_iir_1 = signal.sosfreqz(sos_iir_1, worN=f, fs=fs)
f, h_fir_1 = signal.freqz(num_fir_1, 1, worN=f, fs=fs)

# se grafican ambas respuestas en frecuencia superpuestas
fig1, ax1 = plt.subplots(1, 1, figsize=(10, 7), sharex=True)
ax1.plot(f, 20*np.log10(abs(h_iir_1)), label='Filtro IIR')
ax1.plot(f, 20*np.log10(abs(h_fir_1)), label='Filtro FIR')
ax1.plot([1, 50], [-20, -20], 'X', label='Requisitos de atenuación')
ax1.set_ylabel('Ganancia [dB]', fontsize=15)
ax1.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax1.grid(which='both')
ax1.legend(loc="lower right", fontsize=15)
ax1.set_title('Filtro IIR vs FIR', fontsize=15)
ax1.set_xscale('log')
ax1.set_xlim([0.5, 150])
ax1.set_ylim([-80, 10])

plt.show()

#pyFDA

# se carga el filtro diseñado mediante pyFDA
filtro_iir = np.load('./FiltrosDigitales/filtro_iir.npz', allow_pickle=True)

# podemos recuperar los parámetros del filtro
print("Tipo de filtro {}".format(  filtro_iir['rt']))
print("Aproximación utilizada:" + filtro_iir['creator'][1])
print("Frecuencia de muestreo: {:.1f} Hz".format(filtro_iir['f_S']))
print("Orden del filtro: {:}".format(2*filtro_iir['N']))            # Al ser pasa banda el orden se duplica
print("Frecuencia banda de rechazo inferior: {:.1f} Hz".format(filtro_iir['F_SB']*filtro_iir['f_S']))
print("Frecuencia inferior banda de paso : {:.1f} Hz".format(filtro_iir['F_PB']*filtro_iir['f_S']))
print("Frecuencia superior banda de paso : {:.1f} Hz".format(filtro_iir['F_PB2']*filtro_iir['f_S']))
print("Frecuencia banda de rechazo superior: {:.1f} Hz".format(filtro_iir['F_SB2']*filtro_iir['f_S']))

# Se extraen los coeficientes de numerador y denominador
num_iir_2, den_iir_2 = filtro_iir['ba']
print("Coeficientes numerador:")
print(num_iir_2)
print("Coeficientes denominador:")
print(den_iir_2)

# Se convierte a secciones de orden dos (SOS)
sos_iir_2 = signal.tf2sos(num_iir_2, den_iir_2)
print("Secciones de orden 2:")
print(sos_iir_2)

# se carga el filtro diseñado mediante pyFDA
filtro_fir = np.load('./FiltrosDigitales/filtro_fir.npz', allow_pickle=True)

# podemos recuperar los parámetros del filtro
print("Tipo de filtro {}".format(  filtro_fir['rt']))
print("Aproximación utilizada:" + filtro_fir['creator'][1])
print("Frecuencia de muestreo: {:.1f} Hz".format(filtro_fir['f_S']))
print("Orden del filtro: {:}".format(2*filtro_fir['N']))            # Al ser pasa banda el orden se duplica
print("Frecuencia banda de rechazo inferior: {:.1f} Hz".format(filtro_fir['F_SB']*filtro_fir['f_S']))
print("Frecuencia inferior banda de paso : {:.1f} Hz".format(filtro_fir['F_PB']*filtro_fir['f_S']))
print("Frecuencia superior banda de paso : {:.1f} Hz".format(filtro_fir['F_PB2']*filtro_fir['f_S']))
print("Frecuencia banda de rechazo superior: {:.1f} Hz".format(filtro_fir['F_SB2']*filtro_fir['f_S']))

# Se extraen los coeficientes de numerador y denominador
num_fir_2, den_fir_2 = filtro_fir['ba']
print("Coeficientes numerador:")
print(num_fir_2)
print("Coeficientes denominador:")
print(den_fir_2)

fs = 360

# se genera un vector de frecuencias
f = np.logspace(-1, 3, int(1e3))
# se analiza la respuesta en frecuencia de ambos filtros
f, h_iir_2 = signal.sosfreqz(sos_iir_2, worN=f, fs=fs)
f, h_fir_2 = signal.freqz(num_fir_2, 1, worN=f, fs=fs)

# se grafican ambas respuestas en frecuencia superpuestas
fig1, ax1 = plt.subplots(1, 1, figsize=(10, 7), sharex=True)
ax1.plot(f, 20*np.log10(abs(h_iir_2)), label='Filtro IIR')
ax1.plot(f, 20*np.log10(abs(h_fir_2)), label='Filtro FIR')
ax1.plot([1, 50], [-20, -20], 'X', label='Requisitos de atenuación')
ax1.set_ylabel('Ganancia [dB]', fontsize=15)
ax1.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax1.grid(which='both')
ax1.legend(loc="lower right", fontsize=15)
ax1.set_title('Filtro IIR vs FIR', fontsize=15)
ax1.set_xscale('log')
ax1.set_xlim([0.5, 150])
ax1.set_ylim([-80, 10])

plt.show()
