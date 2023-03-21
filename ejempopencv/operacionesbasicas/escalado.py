import cv2
'''Escalado
El escalado permite obtener una imagen con un tamaño diferente al original
Este es importante cuando se aplican tecnicas de comparacion de imagenes, las cuales se requiern que sena de las
mismas dimensiones.
La funcion a utilizar es :
             resize( imagen, tamaño)

El primer argumento es la imagen que se va ha escalar el segundo es una tupla que fija 
el ancho y el alto de la imagen escalada

'''


img = cv2.imread('medusa.jpg', 1)

alto, ancho, _ = img.shape
escala = 1.5
ancho_escalado, alto_escalado = int(ancho*escala), int(alto*escala)

imagen_escalada = cv2.resize(img, (ancho_escalado, alto_escalado))

cv2.imshow('Imagen original', img)
cv2.imshow('Imagen escalada', imagen_escalada)

cv2.waitKey(0)
cv2.destroyAllWindows()
