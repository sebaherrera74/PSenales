import numpy as np
import matplotlib.pyplot as plt

#Defino funcion delta
def delta(n):
    if n == 0:
        return 1
    else:
        return 0


#Defino las listas

h_ = []
x_ = []
y_ = []
n = 3
es_=[]

#Escribo x[n] en la forma de la funcion delta
for i in range(-n,n+2):
    x = 2*delta(i+3) + 2*delta(i+2)+2*delta(i+1)+0*delta(i)\
        +1*delta(i-1)+2*delta(i-2)+3*delta(i-3)+4*delta(i-4)
    x_.append(x)

print(x_)

for i in range(0,8):
    x_[i]=x_[i-8]

print(x_)

'''
plt.figure(1)
markerline, stemlines, baseline = plt.stem(range(-n,n+2),x_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-5,5])
plt.xlim([-5,5])
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.title('X[n]')
plt.grid(True)
plt.show()
'''

