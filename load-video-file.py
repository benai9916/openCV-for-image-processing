import cv2
# show manage the frame rate
import time

# Load video file
cap = cv2.VideoCapture('data2/finger_move.mp4')


if cap.isOpened() == False:
    print('Error file not found')
    
while cap.isOpened() == True:
    ret, frame = cap.read()
    
    if ret == True:
        
        # deplay by 20fps
        time.sleep(1/20)
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    else:
        break
        
cap.release()
cv2.destroyAllWindows()