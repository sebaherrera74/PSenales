import cv2

img=cv2.imread('/home/sebastian/Imágenes/fotos034.jpg',0)
#cv2.imshow('cuadro',img)

tamanio=img.size
print(tamanio)
print("Tamaño "+ str(tamanio) +" bytes")
cv2.waitKey(0)
cv2.destroyAllWindows()