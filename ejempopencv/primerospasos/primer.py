import cv2

#img=cv2.imread('cuadro.jpg',0) #Carga imagen en BN 
img=cv2.imread('cuadro.jpg',1)  #carga Imagen en color 
cv2.imshow('cuadro',img)

tamanio=img.size

print("Tamaño "+ str(tamanio) +" bytes")
cv2.waitKey(0)
cv2.destroyAllWindows()

#prueba de grafica;