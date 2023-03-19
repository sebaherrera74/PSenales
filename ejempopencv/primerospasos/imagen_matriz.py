import cv2 
import numpy as np

'''matriz= [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         ]
# 0-> Negro
# 1 ->Blanco 


img=np.array(matriz)  #Crea una imagen de a partir de una matriz de 5x5 

print(img)
'''
#cv2.imshow('negra',img) #Fijarse que pasa 

''' Esta forma no es practica de trabajar para eso Numpy tiene las librerias "zeros" y "one'''

'''Creacion de una imagen Negra '''
'''
img=np.zeros((5,5),np.uint8)
print(img)
#Cambiar valor de al,to y ancho y probar 
#Prodria ver el tamaño de la imagen creada 
tamanio=img.size   # de esta manera tambien se saca el tamaño de una imagen 
print("Tamaño: " + str(tamanio) + " bytes")
cv2.imshow('negra',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''Creacion de una imagen Blanca '''
'''
img=np.ones((5,5),np.uint8)*255   #Multiplico por 255 por que el color negro es 255 recordar
print(img)
#Cambiar valor de al,to y ancho y probar 
#Prodria ver el tamaño de la imagen creada 
tamanio=img.size   # de esta manera tambien se saca el tamaño de una imagen 
print("Tamaño: " + str(tamanio) + " bytes")
cv2.imshow('negra',img)


cv2.waitKey(0)
cv2.destroyAllWindows()

'''

'''Creacion de una imagen  color  '''
#En el primer paramtero le agre3go la cantidad de caales recordar 
#que en color es 3 
img=np.ones((3,3,3),np.uint8)   #Multiplico por 255 por que el color negro es 255 recordar

print(img)
#Probar cambiar los valores de las matrices de colores 
#       B  G  R -> Ojo con esto 
#img[:]=(0,0,0)
#img[:]=(100,100,200)
#img[:]=(255,0,0)
#img[:]=(0,255,0)
img[:]=(0,0,255)

print(img)
#Cambiar valor de al,to y ancho y probar 
#Prodria ver el tamaño de la imagen creada 
tamanio=img.size   # de esta manera tambien se saca el tamaño de una imagen 
print("Tamaño: " + str(tamanio) + " bytes")
cv2.imshow('color',img)


cv2.waitKey(0)
cv2.destroyAllWindows()



