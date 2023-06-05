import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy.signal import resample



#fs, x=read("Alarm01.wav") # carga señal de audio

fs, x=read("080EHC_S1_readtext.wav") # carga señal de audio

t=np.arange(len(x))/fs
plt.figure(figsize=(15,6))
plt.plot(t,x)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

#Audio(x,rate=fs)
#Carga el archivowav y muestra la señal continua
#---------------------------------------------
print("El número de muestras es: ", len(x))
print("La frecuencia de muestreo es: ", fs)
print("La longitud en tiempo es: ", len(x)/fs, "segundos")
print(x)
range_s=np.max(np.abs(x))

print("rango de la señal: ", range_s)

bits=np.ceil(np.log2(range_s))+1
print("Número de bits de cuantificación: ", int(bits))

#Probar divindo en 4 como la señal original pierde informacion
#Probar Multiplicando por cuatro la señal es la original

x2=resample(x, int(len(x)/16))
fs2=fs/16

plt.figure(figsize=(15,6))
t=np.arange(len(x))/fs
plt.plot(t,x, label="original")
t2=np.arange(len(x2))/fs2
plt.plot(t2,x2, label="remuestreada")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show()
#print(x2)

amplitude = np.iinfo(np.int16).max

data = x2/amplitude
#print(data)
#write("otro.wav",fs2,data)

