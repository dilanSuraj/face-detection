import cv2 as cv

# Read the video from file
cap = cv.VideoCapture("Soccer.mp4")

while(True):
    ret, frame = cap.read();
    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release();
cv.destroyAllWindows()