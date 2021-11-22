import cv2

#Library to find the face in any photo
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#img = cv2.imread("Saurabh.jpg")
img = cv2.imread("news.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Looking for image
#with every step, it will reduce the size of image with scaleFactor
#minNeighbors - Other objects around face
faces = face_cascade.detectMultiScale(grey_img, scaleFactor = 1.1, minNeighbors = 5)

#Drawing an rectangle on face.
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0),3)

print(type(faces))
print(faces)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
