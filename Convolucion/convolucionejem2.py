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

#Escribo x[n] en la forma de la funcion delta
for i in range(0,n+10):
    x = ((0.5)**i)*escalon(i)
    x_.append(x)

x_=np.array(x_)
print(x_)
print(x_.size)

plt.figure(2)
markerline, stemlines, baseline = plt.stem(range(0,n+10),x_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([0,1])
plt.xlim([-n,n+10])
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.title('$x[n] $')
plt.grid(True)


plt.show()