import cv2
import numpy as np 

'''-----------Utilizacion de algunas funciones de interaccion con el mouse------
Se utiliza la funcion 
      setMouseCallback(ventana,funcion)
   El primer argumento es nombre d ela ventatacon el que se van ha capturar los eventos del mouse
   Y el segundo corresponde a la funciond e callback encargada de manejarlos.Se podria utilizar una
   tecer argumento para pasar argumentos adicionales cuando se produce el evento   
   -La funcion de callback se debeb declarar con los siguientes argumentos :

          funcion de callback (evento,x,y,flags)
   
    El primer argumento es el evento generado representado por las constantes:

    EVENT_LBUTTONDBLCLK: Doble click con el boton izquierdo del raton 
    EVENT_LBUTTONDOWN: Se ha presionado el boton izquierdo del raton
    EVENT_LBUTTONUP: Se deja de presionar el boton izquierdo del raton 
    EVENT_MBUTTONDBLCLK: Doble click con el boton central del raton 
    EVENT_MBUTTONDOWN: Se ha presionado el boton central del raton 
    EVENT_MBUTTONUP:  Se deja de presionar el boton central del raton 

    EVENT_MOUSEHWHEEL: Los valores positivos y negativos indican el desplazamiento 
    hacia la derecha o hacia la izquierda de la rueda del raton 
    EVENT_MOUSEMOVE El puntero  del raton se ha movido
    EVENT_MOUSEWHEEL: Los valores positivos y negativos indican el desplazamiento 
    hacia adelante o hacia atras de la rueda del raton 
    EVENT_RBUTTONDBLCLK:  Doble click con el boton derecho del raton 
    EVENT_RBUTTONDOWN: Se ha presionado el boton derrecho del raton 
    EVENT_RBUTTONUP: Se deja de presionar el boton derecho del raton 

Los dos argumentos sigueintes x e y son las coordenadas del punto en el que se ncontraba el raton cuando se produjo el evento.

El evento flag indica diferentes situaciones especiales 
EVENT_FLAG_ALTKEY:  La tecla ALT esta presionada 
EVENT_FLAG_CTRLKEY: la tecla CTRL esta presionada
EVENT_FLAG_LBUTTON: El boton izquierdo del raton esta presionado 
EVENT_FLAG_MBUTTON: El boton central del raton esta presionado 
EVENT_FLAG_RBUTTON: El boton derehcho del raton esta presionado 
EVENT_FLAG_SHIFTKEY: La tecla SHIFT esta presionada 

 '''




img = np.ones((600, 600, 3), np.uint8)
img[:] = (255, 255, 255)

color = (0, 0, 255)
grosor = 4
fuente = cv2.FONT_HERSHEY_SIMPLEX
escala = 1

cv2.imshow('Eventos raton', img)

def eventos_raton(evento, x, y, flags, parametros):
    if evento == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img, "Clic izquierdo", (x, y), fuente, escala, color, grosor)
    elif evento == cv2.EVENT_RBUTTONDOWN:
        cv2.putText(img, "Clic derecho", (x, y), fuente, escala, color, grosor)

    cv2.imshow('Eventos raton', img)
    

cv2.setMouseCallback('Eventos raton', eventos_raton)


key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()
