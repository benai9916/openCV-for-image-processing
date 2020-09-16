import cv2

cap = cv2.VideoCapture(1)


# CALL BACK FUNCTION RECTANGLE
def draw_rectangle(event, x, y, flags, params):
    
    global pt1, pt2, topLeft_Clicked, bottomRight_Clicke
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # reset the rectangle 
        if topLeft_Clicked == True and bottomRight_Clicke == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_Clicked = False
            bottomRight_Clicke = False
            
        if topLeft_Clicked == False:
            pt1 = (x, y)
            topLeft_Clicked = True
            
        elif bottomRight_Clicke == False:
            pt2 = (x,y)
            bottomRight_Clicke = True


    
# GLOBAL VARIABLE
pt1 = (0,0)
pt2 = (0,0)
topLeft_Clicked = False
bottomRight_Clicke = False

#  CONNECT TO CALL BACK
cv2.namedWindow(winname='frame')

cv2.setMouseCallback('frame', draw_rectangle)


while cap.isOpened() == True:
    
    ret, frame = cap.read()
    
    # DRAW ON THE FRAME BASE ON THE GLOBAL VARIABLE 
    if topLeft_Clicked:
        cv2.circle(frame, pt1, 5, (255, 0, 0), -1)
        
    if topLeft_Clicked and bottomRight_Clicke:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), 3)
        
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
                        