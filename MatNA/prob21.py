#Trabajo Parctico Numero 2 Matematica Numerica Avanzada 
#Problema 2.1 

import numpy as np

# Defino la función f(m) basada en la ecuación dada
def f(m, g=9.8, c=15, v=30, t=7):
    return (g * m / c) * (1 - np.exp(-c * t / m)) - v

# Método de falsa posición
#Le paso como parametros la funcion f, los valores m1 y m2 de supuestas masas probables,
#la tolerancia y la cantidad maxima de iteracciones.
#Me devuelve el resultado de la masa, con el error que se calculo y el numero de
#iteraciones 
def falsa_posicion(f, m1, m2, tol, max_iter=100):
    f_m1 = f(m1)
    f_m2 = f(m2)
    if f_m1 * f_m2 > 0:
        raise ValueError("La función no cambia de signo en los puntos dados")
    
    for i in range(max_iter):
        #print(i)
        # Calcular el nuevo punto usando la fórmula de falsa posición
        m_nuevo = m2 - f_m2 * (m2 - m1) / (f_m2 - f_m1)
        f_nuevo = f(m_nuevo)
        
        # Calcular el error relativo
        error_relativo = abs((m_nuevo - m2) / m_nuevo) *100
        #print(error_relativo)
        
        # Si el error es menor que la tolerancia, terminamos
        if error_relativo < tol:
            #print("aqui")
            return m_nuevo, error_relativo, i+1
           
        
        # Actualizar los valores para la siguiente iteración
        if f_nuevo * f_m1 < 0:
            m2, f_m2 = m_nuevo, f_nuevo
        else:
            m1, f_m1 = m_nuevo, f_nuevo
    
    return m_nuevo, error_relativo, max_iter

# Definir los valores iniciales de m1 y m2 (valores razonables para la masa en kg)
m1 = 50  # suposición inicial más baja
m2 = 100  # suposición inicial más alta

# Aplicar el método de falsa posición
m_resultado, error, iteraciones = falsa_posicion(f, m1, m2, tol=0.1)

print(m_resultado, error, iteraciones)
