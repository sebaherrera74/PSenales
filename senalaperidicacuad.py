import numpy as np
import matplotlib.pyplot as plt


def clear():
    print ("\n" * 50)

plt.clf()
clear() 
pure=np.array([1, 0, 1, 1, 1, 0, 0, 1, 0, 1 ])
noise = np.random.normal(0.2, 0.4, pure.shape)
signal = pure + noise
final=[]
t=0.5
for x in range (len(pure)):
    if (signal[x] > t):
        final.append(1)
    else :
        final.append(0)
print(pure)
print(signal)
print(final)

plt.subplot(1,1,1)
plt.title('Señal final')
plt.ylabel('Voltaje (V)')
plt.xlabel('Tempo (s)')
p=[1,2,3,4,5,6,7,8,9,10]
plt.plot(p,final, drawstyle='steps-mid')
plt.show()

plt.title('Señal inicial')
plt.ylabel('Voltaje (V)')
plt.xlabel('Tempo (s)')
p=[1,2,3,4,5,6,7,8,9,10]
plt.plot(p,pure,drawstyle='steps-mid')
plt.show()

plt.subplot(1,1,1)
plt.title('Señal con ruidol')
plt.ylabel('Voltaje (V)')
plt.xlabel('Tempo (s)')
p=[1,2,3,4,5,6,7,8,9,10]
plt.plot(p,signal,drawstyle='steps-mid')
plt.show()