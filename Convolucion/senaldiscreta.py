import numpy as np
import matplotlib.pyplot as plt
#Ejemplo de una señal discreta

#n=[]
#n=np.array(n)
#print(type(n))

n=np.arange(0,10,1)

#print(n)
#print(np.size(n))

x=np.array([-2,1,5,0,2,3,-3,0,0,0])
#print(x)

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
"""
#X=[]

for i in range(0,10):
    aux=(-2)*delta(i)+1*delta(i-1)+5*delta(i-2)\
        +2*delta(i-4)+3*delta(i-5)+(-3)*delta(i-6)
    X.append(aux)

print(X)

plt.stem(n,X)
plt.show()

"""
#Crear una funcion en l cual le pase como parametro un arreglo y me cree 
#una señal discreta en 

def discretFun(array, delta):
    X=[]

    for i in range(0,10):
        aux=(-2)*delta(i)+1*delta(i-1)+5*delta(i-2)\
        +2*delta(i-4)+3*delta(i-5)+(-3)*delta(i-6)
    X.append(aux)
    return X
  

A=discretFun(x,delta)
print(A)


#a=delta(0)
#print(a)

#b=escalon(-2)
#print(b)

#plt.stem(n,x)
#plt.show()


'''
n=np.array(n)
print(type(n))

n=np.arange(-3,10,1)

print(n.size)
x=np.array([-2,1,1,0,3,4,5])
print(np.size(x))

for i in range(n.size-x.size):
    x=np.append(x,0)

print(np.size(x))
print(x)

plt.stem(n,x, '--')
plt.ylim([-4,8])
plt.xlim([-4,15])
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.title('$ x[n] $')
plt.grid(True)
plt.show()


x=[-2,1,1,0,3,4,5]
print(x)
print(len(x))
#x=x*n  #no se puede multiplicar son de diferentes tamaños

for i in range(n.size-len(x)):
    x.append(1)


#print(len(x))
plt.stem(n,x, '--')
plt.ylim([-2,2])
plt.xlim([-4,4])
plt.xlabel('$n$')
plt.ylabel('$[n]$')
plt.title('$y[n] $')
plt.grid(True)
plt.show()



y=0.5*n

print(type(y))

print(y)

plt.stem(n,y, '--')
plt.ylim([-2,2])
plt.xlim([-4,4])
plt.xlabel('$n$')
plt.ylabel('$y[n]$')
plt.title('$y[n] $')
plt.grid(True)
plt.show()
'''
