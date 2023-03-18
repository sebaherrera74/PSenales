import cv2 

#img=cv2.imread('cuadro.jpg',0) #Carga imagen en BN 
img = cv2.imread('cuadro.jpg', 1)
cv2.imshow('Cuadro', img)

'''Las imagenes se almacenan como matrices de pixeles en objetos de la clase ndarray, de las cuales se 
pueden extraer sus caracteristicas claves como su dimension, el numero de canales( BN 1 canal, Color 3 canales
uno por cada color primario) , el tipod edato con el que se almacena y el tamañao que ocupa en el disco.

Se accede a sus mediante "shape" , esto me da una tupla con tres valores (alto,ancho,n canales) 

Para calcular el tamaño de una imagen =ancho x alto x nro de canales
'''
tamanio = img.size   # de esta manera tambien se saca el tamaño de una imagen 
alto, ancho, canales = img.shape   #atributos de la imagen
tipo = img.dtype
print("Tamaño: " + str(tamanio) + " bytes")
print("Ancho: " + str(ancho) + " píxeles")
print("Alto: " + str(alto) + " píxeles")
print("Nº canales: " + str(canales))
print("Tipo: " + str(tipo))

cv2.waitKey(0)
cv2.destroyAllWindows()