import cv2

img = cv2.imread('cuadro.jpg', 1)
img_original = img.copy()

cv2.imshow('Cuadro', img)

color = img[3, 4].tolist()

print(color)

def color(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        a=100
        print(a)
    elif event == cv2.EVENT_LBUTTONUP:
        img = img_original.copy()
    cv2.imshow('Cuadro',img)

cv2.setMouseCallback('Cuadro',color)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
