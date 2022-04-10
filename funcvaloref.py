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

ns = [10,50,100]
doblar_valores(ns)
print(ns)

