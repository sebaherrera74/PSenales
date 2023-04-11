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
es_=[]

for i in range(-n,n+10):
    es=0*delta(i)+0*delta(i-1)+delta(i-2)\
    +delta(i-3)+delta(i-4)+delta(i-5)\
    +delta(i-6)+delta(i-7)+delta(i-11)\
    +delta(i-12)+delta(i-13)+delta(i-14)\
    +delta(i-15)+delta(i-16)
    h_.append(es)

h_=np.array(h_)
print(h_)
print(h_.size)

#Escribo x[n] en la forma de la funcion delta
for i in range(-n,n+10):
    x = delta(i) + delta(i-1)+delta(i-2)\
        +delta(i-3) + delta(i-4)+delta(i-5)
    x_.append(x)

x_=np.array(x_)
print(x_)
print(x_.size)

#Convolucion lineal de las 2 funciones#
y_ = np.convolve(x_,h_,mode='full')
print(y_)
print(y_.size)

x=np.arange(6,53)
print(x)
print(x.size)


plt.figure(1)
markerline, stemlines, baseline = plt.stem(range(-n,n+10),h_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-3,3])
plt.xlim([-n,n+10])
plt.xlabel('$n$')
plt.ylabel('$h[n]$')
plt.title('h[n]')
plt.grid(True)


plt.figure(2)
markerline, stemlines, baseline = plt.stem(range(-n,n+10),x_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-6,6])
plt.xlim([-n,n+10])
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.title('$x[n] $')
plt.grid(True)


#Plotting the y[n] function

plt.figure(3)
plt.stem(x, y_ ,'--')
#plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
#plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-7,7])
plt.xlim([0,50])
plt.xlabel('$n$')
plt.ylabel('$y[n]$')
plt.title('$y[n]$')
plt.grid(True)

plt.show()

