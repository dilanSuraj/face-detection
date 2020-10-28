import cv2 as cv

# Read the image
img = cv.imread("images/Ronaldo-1.jpg")

# Read the image, greyscale
# img = cv.imread("images/Ronaldo-1.jpg", 0)

# This will preview the image
cv.imshow("Image", img)

enteredKey = cv.waitKey()

# ASCII code for 'Esc' is 27
if enteredKey == 27:
    cv.destroyAllWindows()
# s key
elif enteredKey == ord("s"):
    cv.imwrite("Images/new-Ronaldo-1-s.jpg", img)
    cv.destroyAllWindows()