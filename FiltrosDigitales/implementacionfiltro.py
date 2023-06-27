import wfdb

# Incluir librerías
from scipy import signal, fft
import numpy as np
import matplotlib.pyplot as plt

# carga de la señal utilizando el paquete WFDB
record = wfdb.rdrecord('300', pn_dir='stdb')
wfdb.plot_wfdb(record=record, time_units='seconds', figsize=(15, 7),
               title='Registro 300 - MIT-BIH ST Change Database')

print("Parámetros del registro:")
print(f"- Nombre del registro: {record.record_name}")
print(f"- Cantidad de señales: {record.n_sig}")
print(f"- Frecuencia de muestreo: {record.fs}")
print(f"- Longitud de las señales: {record.sig_len}")
