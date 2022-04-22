
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def fxquant(s,bit):
    # s: senal de entrada
    # bit: bits de cuantificación
    Plus1=np.power(2, (bit-1))
    X=s*Plus1
    X=np.round(X)
    X=np.minimum(Plus1-1.0,X)
    X=np.maximum(-1.0*Plus1,X)
    X=X/Plus1
    return X

fs, x=read("Alarm01.wav") # carga señal de audio
#fs, x=read("080EHC_S1_readtext.wav") # carga señal de audio

x=x/np.max(np.abs(x))


x_req=fxquant(x, 2)

plt.figure(figsize=(15,5))
t=np.arange(len(x))/fs
plt.plot(t,x, label="Señal original",alpha=0.7)#
#plt.plot(t,x_req, label="Señal re-cuantizada",alpha=0.7)
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()

plt.figure(figsize=(15,5))
t=np.arange(len(x))/fs
plt.plot(t[0:3200],x[0:3200], label="Señal original",alpha=0.7)
#plt.plot(t[0:3200],x_req[0:3200], label="Señal re-cuantizada",alpha=0.7)
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()