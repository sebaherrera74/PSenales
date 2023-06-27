import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sfft
import scipy.signal as win



f0=1
Fs=50
Ts= 1/Fs
arregloY =np.arange(0.0, 20.0,1)
arregloX =np.arange(0.0, 20.0,1)
#print(arregloY)

n = np.arange(0, 40, step=2/Fs)
x_n = np.cos(2*np.pi*f0*Ts*n)

x_n_1 = np.cos(2*np.pi*f0*Ts*(n-1))

#Forma general del filtro es y(n)=x(n)+g*x(n-r)



y_n=x_n + x_n_1       #Filtro pasa bajo
#y_n=x_n - 2*x_n_1       #Filtro pasa alto


#---------------------Máximo

max = np.max(x_n)

print(f"El máximo de la señal es de {max:.5f}V")

max = np.max(y_n)

print(f"El máximo de la señal es de {max:.5f}V")

for i in range(20):
    f0=i
    #print(f0)
    x_n = np.cos(2*np.pi*f0*Ts*n)
    x_n_1 = np.cos(2*np.pi*f0*Ts*(n-1))
    y_n=x_n + x_n_1
    maximoY = np.max(y_n)
    print(f"El valor máximo de la señal de salida es de {maximoY:.5f}V")
    maximoX = np.max(x_n)
    print(f"El valor máximo de la señal de entrada es de {maximoX:.5f}V")
    arregloY[i]=   maximoY
    arregloX[i]=   maximoX

print (arregloY)
print (arregloX)

n1= np.arange(0, 20, 1)
plt.plot(n1,arregloY)
plt.plot(n1,arregloX)
plt.show()


plt.figure(figsize=(15,5))



plt.plot(n,x_n, 'r')
plt.plot(n,x_n_1, 'black')

plt.plot(n,y_n, 'b')
plt.xlabel("tiempo")
plt.ylabel("Amplitud")
#plt.legend()
plt.grid()
plt.show()
