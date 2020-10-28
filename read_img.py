import cv2 as cv

# Read the image
img = cv.imread("images/Ronaldo-1.jpg")

# Read the image, greyscale
# img = cv.imread("images/Ronaldo-1.jpg", 0)

# This will preview the image
cv.imshow("Image", img)

# delay
cv.waitKey(delay=1000)
cv.destroyAllWindows()