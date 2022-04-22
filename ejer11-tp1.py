
def elimina(lista):
    nuevalista=[]
    tamanoLista=len(lista)
    #print(tamanoLista)
    lista.pop(0)
    lista.pop(-1)
    nuevalista=lista
    #print(nuevalista)
    return nuevalista




lista1=[1,2,3,4,5]
lista1=[-11,2,3,4,5,6,7,8,9,10]
#lista2=['enero','febrero','marzo','abril']

resultadolista=elimina(lista1)
#resultadolista2=elimina(lista2)

print(resultadolista)
#print(resultadolista2)
#nuevalista=[2,3,4]
