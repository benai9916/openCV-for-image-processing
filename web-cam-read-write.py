import numpy as np
import cv2

cap = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# saving a video
writer  = cv2.VideoWriter('my_vuideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Sve the video
    writer.write(frame)
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('frame',gray)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# When everything done, release the capture
cap.release()
writer.release()
cv2.destroyAllWindows()