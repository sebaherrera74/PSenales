import cv2 
  
img1 = cv2.imread('espacio.jpg', 1)
#img2 = cv2.imread('medusa.jpg', 1)


img2 = cv2.imread('tierra.jpg', 1)

tamanio = img1.size
tamanio2 = img2.size  
alto, ancho, canales = img2.shape
print(tamanio)
print(tamanio2)
print(alto,ancho,canales)

img = cv2.addWeighted(img1, 0.4, img2, 0.8, 0)

cv2.imshow('Composicion imagenes', img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()