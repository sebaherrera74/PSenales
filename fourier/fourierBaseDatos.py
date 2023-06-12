"""Ejemplo del uso de Fourier en una base de datos"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
import pandas as pd

df = pd.read_csv('./fourier/dataexport.csv',delimiter=',', parse_dates=[1])

df.rename(columns={'Timestamp (Hour Ending)':'hour','Demand Forecast (MWh)':'demand'},inplace=True)
plt.figure(figsize = (12, 6))
plt.plot(df['hour'], df['demand'])
plt.xlabel('Datetime')
plt.ylabel('California electricity demand (MWh)')
plt.xticks(rotation=25) 
plt.show()


print(df['demand'])

X = fft(df['demand'])
N = len(X)
n = np.arange(N)
# get the sampling rate
sr = 1 / (60*60)
T = N/sr
freq = n/T 

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

plt.figure(figsize = (12, 6))
plt.plot(f_oneside, np.abs(X[:n_oneside]), 'b')
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.show()

"""Vemos algunos picos claros en la figura de amplitud FFT, pero es difícil decir cuáles 
son en términos de frecuencia. Tracemos los resultados usando horas y resaltemos algunas 
de las horas asociadas con los picos.
"""

# convert frequency to hour
t_h = 1/f_oneside / (60 * 60)

plt.figure(figsize=(12,6))
plt.plot(t_h, np.abs(X[:n_oneside])/n_oneside)
#plt.xticks([12, 24, 84, 168])
plt.xlim(0, 200)
plt.xlabel('Period ($hour$)')
plt.show()


#ra1w_data = open('./fourier/DemandaYTemperatura_05062023.csv')
#data = np.loadtxt(raw_data, dtype='str,int', delimiter=';',skiprows=2, usecols=(0,1), unpack=True)
"""
data=np.loadtxt(raw_data, dtype='str,int',delimiter=";",skiprows=1,usecols=(0,2), unpack=True)
data=np.array(data)
print(data)
print(type (data))
print(data.shape)
"""

