esPar=["val_1","val_2","val_3","val_4","val_5","val_6","val_7","val_8","val_9","val_10"]
A=0
B=0
for i in range(0,10):
    print("VariableN°",i+1)
    esPar[i]=input('IngreseValor=')
    esPar[i]=float(esPar[i])
    Division=(esPar[i])%2
    if Division==0:
        print("True")
        A=esPar[i]+A
    else:
        print("False")
        B=esPar[i]+B

print("Sumatoria numeros pares=", A)
print("Sumatoria numeros impares=",B)
