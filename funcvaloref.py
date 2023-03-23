'''
#Funcion para paso por valor
def doblar_valor(numero):
    numero =numero*2
    r=numero
    return r
'''



#n = 10
#resultado=doblar_valor(n)
#print(resultado)


#funcion para paso por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] = numeros[i]*2
    return n




ns = [10,50,100]
nf=[1,5,10,15,20,25,30,40]
a=doblar_valores(ns)
b=doblar_valores(nf)
print(ns)
print(a)  

print(nf)
print(b)   