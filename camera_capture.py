import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpend()):
    ret,frame = cap.read()

    cv2.imshow("Camera",frame)

    if(cv2.waitkey(1) & 0xff == ord('q')):
        bread

cap.release()
cv2.destroyAllWindows()

