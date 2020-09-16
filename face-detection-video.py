import cv2

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

def detect_face(img):
    
    face_img = img.copy()
    
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor =1.2, minNeighbors = 5)
    
    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w, y+h), (255, 0, 0), 10)
        
    return face_img



cap = cv2.VideoCapture(1)

while True:
    res, frame = cap.read()
    
    result = detect_face(frame)
    
    cv2.imshow('frame', result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()