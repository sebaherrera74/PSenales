
def sumaAcumulada(lista):
    listaAuxiliar=[]
    sumavalores=0
    for iter in lista:
        #print(iter)
        sumavalores=sumavalores+iter
        #print(sumavalores)
        listaAuxiliar.append(sumavalores)
       
    return listaAuxiliar



#listadeprueba=[1,2,3,4,5]
listadeprueba2=[20,42,3,4,5,6,7,8,9]

listadeprueba3=[-20,-42,0,1000,5,6,7,8,9]
#sumaAcumulada(listadeprueba)
aux=sumaAcumulada(listadeprueba2)
aux1=sumaAcumulada(listadeprueba3)

print(aux)
print(aux1)

#resultado=[1,3,6,10,15]

