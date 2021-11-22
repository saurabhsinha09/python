import cv2, time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    #print(check)
    #print(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("CAM", gray)
    keyboard = cv2.waitKey(1)

    if keyboard == ord('q'):
        break

video.release()
cv2.destroyAllWindows()