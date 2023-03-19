import cv2 
  
img = cv2.imread('figuras_geometricas.png',1)

img_azul,img_verde, img_roja = cv2.split(img)

#print(img_azul)
cv2.imshow('cuadro', img)
cv2.imshow('Azul', img_azul)
cv2.imshow('Verde', img_verde)
cv2.imshow('Roja', img_roja) 

cv2.waitKey(0)

cv2.destroyAllWindows()