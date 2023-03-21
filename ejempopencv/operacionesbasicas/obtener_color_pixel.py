import cv2

img = cv2.imread('cuadro.jpg', 1)
img_original = img.copy()

cv2.imshow('Cuadro', img)

def color(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        color = img[y, x].tolist()
        cv2.circle(img, (x, y), 40,color, -1)
        #print(color)
    elif event == cv2.EVENT_LBUTTONUP:
        img = img_original.copy()
    cv2.imshow('Cuadro',img)

cv2.setMouseCallback('Cuadro',color)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()
