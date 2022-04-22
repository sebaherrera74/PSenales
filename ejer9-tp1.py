
def esPar(numero):
    auxiliar=numero%2

    if (auxiliar==0):
        return True #si el numero es par 
    else:
        return False #si el numero es impar   


#numero1=4
#resultado=esPar(numero1)
#print(resultado)
#numero2=5
#resultado1=esPar(numero2)
#print(resultado1)

sumapar=0.0
sumaimpar=0.0

for iter in range(10):
    valoringresado=int(input("Ingrese valor :"))
    #print(valoringresado)
    if(esPar(valoringresado)):
        sumapar=sumapar+valoringresado
    else:
        sumaimpar=sumaimpar+valoringresado

print(sumapar)
print(sumaimpar)


    
    














