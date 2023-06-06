"""Ejemplo del uso de Fourier en una base de datos"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
import pandas as pd

#df = pd.read_csv('./fourier/DemandaYTemperatura_05062023.csv',delimiter=',', parse_dates=[2])

#df.rename(columns={'Timestamp (Hour Ending)':'hour','Total CAL Demand (MWh)':'demand'},inplace=True)

raw_data = open('./fourier/DemandaYTemperatura_05062023.csv')
#data = np.loadtxt(raw_data, dtype='str,int', delimiter=';',skiprows=2, usecols=(0,1), unpack=True)

data=np.loadtxt(raw_data, dtype='str,int',delimiter=";",skiprows=1,usecols=(0,2), unpack=True)
data=np.array(data)
print(data)
print(type (data))
print(data.shape)