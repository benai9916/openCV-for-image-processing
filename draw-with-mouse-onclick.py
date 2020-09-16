import cv2
import numpy as np

#####################
### Function #########
###################

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 30, (222,43, 0), -1) 
        
    # another event
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 12, (255, 0,0), -1)

    
# connect the window to show image
cv2.namedWindow(winname = 'drawing')

# connect to call back
cv2.setMouseCallback('drawing', draw_circle)


######################
### Show image #######
######################

# generate black image
img = np.zeros((400, 600, 3))

while True:
    cv2.imshow('drawing', img)
    
    if cv2.waitKey(27) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()