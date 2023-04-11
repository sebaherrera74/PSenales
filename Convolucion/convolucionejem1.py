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

for i in range(-n,n+1):
    es=escalon(i)-escalon(i-3)
    print(es)
    es_.append(es)

print(es_)

#Escribo x[n] en la forma de la funcion delta
for i in range(-n,n+1):
    x = 0.5*delta(i) + 2*delta(i-1)
    x_.append(x)

print(x_)

#Convolucion lineal de las 2 funciones
y_ = np.convolve(x_,es_,mode='full')

plt.figure(1)
markerline, stemlines, baseline = plt.stem(range(-n,n+1),es_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-3,3])
plt.xlim([-n,n])
plt.xlabel('$n$')
plt.ylabel('$h[n]$')
plt.title('h[n]')
plt.grid(True)



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


'''
#Writing the h[n] function in terms of delta function
for i in range(-n,n+1):
    h = delta(i) - delta(i-1) + delta(i-4) + delta(i-5)
    h_.append(h)

#Writing the x[n] function in terms of delta function
for i in range(-n,n+1):
    x = delta(i-1) + delta(i) + 2*delta(i+1) + delta(i+2)
    x_.append(x)

#Linearly Convolving the two functions
y_ = np.convolve(x_,h_,mode='full')

#Plotting the h[n] function
plt.figure(1)
markerline, stemlines, baseline = plt.stem(range(-n,n+1),h_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-6,6])
plt.xlim([-n,n])
plt.xlabel('$n$')
plt.ylabel('$h[n]$')
plt.title('$h[n] = \delta [n] - \delta [n-1] + \delta [n-4] + \delta [n-5] $')
plt.grid(True)

#Plotting the x[n] function
plt.figure(2)
markerline, stemlines, baseline = plt.stem(range(-n,n+1),x_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-6,6])
plt.xlim([-n,n])
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.title('$x[n] = \delta [n+2] + 2\delta [n+1] + \delta [n] + \delta [n-1]$')
plt.grid(True)

#Plotting the y[n] function
plt.figure(3)
markerline, stemlines, baseline = plt.stem(range(-2*n,2*n+1),y_, '--')
plt.setp(stemlines, 'color', 'b', 'linewidth', 2)
plt.setp(baseline, 'color', 'b', 'linewidth', 0.5)
plt.ylim([-6,6])
plt.xlim([-n,n])
plt.xlabel('$n$')
plt.ylabel('$y[n]$')
plt.title('$y[n] = \delta [n+2] + \delta [n+1] -\delta [n] + 3\delta [n-3] + 3\delta [n-4] + 2\delta [n-5] + \delta [n-6] $')
plt.grid(True)

plt.show()



n=np.arange(-3,6)
print(n)
l=[0,0,0,0,0.5,2,0,0,0]
y=np.array(l)
print(y)

m=[0,0,1,1,1,0,0,0,0,0]
h=np.array(m)


conv=np.convolve(h,y)
print(conv)'''