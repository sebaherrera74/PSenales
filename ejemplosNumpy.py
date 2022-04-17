import numpy as np

sample_list = [1.0, 2.0, 3.0]

a=np.array(sample_list)

print(a)
print(type(a))

#arange()
b=np.arange(0,5)
print(b)

c=np.arange(1,11,1)  #Tamaño de paso ojo
print(c)

#np.arange(1,11,2)
'''
Hay muchas situaciones en las que tienes un rango de números y te gustaría dividir por 
igual ese rango de números en intervalos. El método linspace de NumPy está diseñado para
resolver este problema. linspace tiene tres argumentos:

    El inicio del intervalo
    El fin del intervalo
    El número de subintervalos en los que deseas que se divida el intervalo
'''
d=np.linspace(0, 1, 10) #Probar con 100, 1000, 5 etc.
print(d)

''' Numeros aleatorios ''' 

e=np.random.rand(10)
print(e)

#Devuelve una muestra de números aleatorios entre 0 y 1.

#El tamaño de la muestra puede ser un número entero (para un arreglo unidimensional)
#  o dos enteros separados por comas (para un arreglo bidimensional).

f=np.random.randn(10)
print(f)
#Devuelve una muestra de números aleatorios entre 0 y 1, siguiendo la distribución normal
#El tamaño de la muestra puede ser un número entero (para un arreglo unidimensional)
#  o dos enteros separados por comas (para un arreglo bidimensional).

g=np.random.randint(0, 100, 10)
print(g)
#np.random.randint(low, high, sample_size)

#Devuelve una muestra de números enteros que son mayores o iguales que 'low' y 
# menores que 'high' 

#devuelve el numero maximo del arreglo 
maximo=g.max()
print(maximo)

#devuelve la ubicacion del numero maximo del arreglo 
ubicacion=g.argmax()
print(ubicacion)


