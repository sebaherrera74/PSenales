
import scipy.signal as sg
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

# para listar las variables que hay en el archivo
sio.whosmat('./FiltrosDigitales/ecg.mat')
mat_struct = sio.loadmat('./FiltrosDigitales/ecg.mat')

ecg_one_lead = np.transpose(mat_struct['ecg_lead'])

print(ecg_one_lead)
print(len(ecg_one_lead))
samp_frec = 1000 # Hz
nyq_frec = samp_frec / 2



# filter design

ws1 = 1 #Hz
wp1 = 3 #Hz
wp2 = 15 #Hz
ws2 = 35 #Hz

filter_type = 'butter'
#filter_type = 'ellip'
#filter_type = 'cheby1'

bp_sos = sg.iirdesign(wp=np.array([wp1, wp2]) / nyq_frec, ws=np.array([ws1, ws2]) / nyq_frec, gpass=0.5, gstop=40., analog=False, ftype=filter_type, output='sos')

w, h = sg.sosfreqz(bp_sos)

plt.figure(2)

plt.title('Digital filter frequency response')
plt.plot(w, 20*np.log10(np.abs(h)))
plt.title('Digital filter frequency response')
plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Frequency (rad/sample)')
plt.grid()
plt.show()

