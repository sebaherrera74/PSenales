import numpy as np
import matplotlib.pyplot as plt

#Defino funcion delta
def delta(n):
    if n == 0:
        return 1
    else:
        return 0

#Defino funcion escalon
def escalon(n):
    if n>=0:
        return 1
    else:
        return 0


#Defino las listas
h_ = []
x_ = []
y_ = []
n = 7
hn_=[]

for i in range(-n,n+1):
    aux=escalon(i)-escalon(i-3)
    hn_.append(aux)

#Para la grafica
plt.figure(1)
markerline, stemlines, baseline = plt.stem(range(-n,n+1),hn_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-3,3])
plt.xlim([-n,n])
plt.xlabel('$n$')
plt.ylabel('$h[n]$')
plt.title('h[n]')
plt.grid(True)


#Escribo x[n] en la forma de la funcion delta
for i in range(-n,n+1):
    aux= 0.5*delta(i) + 2*delta(i-1)
    x_.append(aux)

#print(x_)
plt.figure(2)
markerline, stemlines, baseline = plt.stem(range(-n,n+1),x_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-6,6])
plt.xlim([-n,n])
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.title('$x[n] $')
plt.grid(True)


#Convolucion lineal de las 2 funciones

y_ = np.convolve(x_,hn_,mode='full')

print(y_)
print(y_.size)


#Plotting the y[n] function
plt.figure(3)
markerline, stemlines, baseline = plt.stem(range(-2*n,2*n+1),y_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-6,6])
plt.xlim([-n,n])
plt.xlabel('$n$')
plt.ylabel('$y[n]$')
plt.title('$y[n]$')
plt.grid(True)
plt.show()



