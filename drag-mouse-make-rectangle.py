import cv2
import numpy as np


# VARAIBLE

# TRUE while mouse button DOWN and FALSE while mouse button is UP
drawing = False
ix = -1
iy = -1


# function to draw a rectnagel
def draw_rectangle(event, x, y, flags, parms):
    
    global drawing, ix, iy
    
    if event ==  cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 1), -1)
            
    # stop drawing
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 1), -1)

    
# connec to the window
cv2.namedWindow(winname='drag_n_draw')

# call back to the function
cv2.setMouseCallback('drag_n_draw', draw_rectangle)

# create blank image
img = np.zeros((400,600, 3))

# read image
while True:
    
    cv2.imshow('drag_n_draw', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()