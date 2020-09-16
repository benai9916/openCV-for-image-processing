import numpy as np
import cv2


# Lucas-Kanade function

# corner detection params
corner_track_parms = dict( maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7 )

# params for Lucas-kanade optical flow function
lk_params = dict(winSize = (200, 2000), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


cap = cv2.VideoCapture(1)

ret, prev_frame = cap.read()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# track previous point
prevPts = cv2.goodFeaturesToTrack(prev_gray, mask = None, **corner_track_parms)


mask = np.zeros_like(prev_frame)

while True:
    
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # calculate the optical flow on the gray scale
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, gray, prevPts, None, **lk_params)
    
    good_news = nextPts[status == 1]
    good_prev = prevPts[status == 1]
    
    for i, (new, prev) in enumerate(zip(good_news, good_prev)):
        
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()
        
        mask = cv2.line(mask, (x_new, y_new), (x_prev, y_prev), (0,255, 0), 3)
        
        frame == cv2.circle(frame, (x_new, y_new), 8, (255, 0, 0), -1)
    
    img = cv2.add(frame, mask)
    
    cv2.imshow('tracking', img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        
        
    prev_gray = gray.copy()
    prevPts = good_news.reshape(-1,1,2)
    
cv2.destroyAllWindows()
cap.release()