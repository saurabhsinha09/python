#Importing opencv library
import cv2

#Reading an image as grey image
#second parameter in imread method will decide colour.
#0 - gray scale, 1 - Colour
img = cv2.imread("galaxy.jpg", 0)

#Data is type of n dimension array
print(type(img))
print(img)
#Finding row and column of image.
print(img.shape)
#Dimension of image
print(img.ndim)

#Reducing dimension of image by half
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

#Display image
cv2.imshow("Galaxy", resized_image)

#Write resized image in new file
cv2.imwrite("galaxy_resize.jpg", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()