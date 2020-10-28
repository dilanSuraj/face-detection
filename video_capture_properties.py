import  cv2 as cv

# 0 - Webcam
# 1 - Camera 1
# 2 - Camera 2

cap = cv.VideoCapture(0)

print(cap.isOpened())

# isOpened returns true if the camera initialized successfully
while(cap.isOpened()):

    ret, frame = cap.read()

    # print frame's height and width
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv.destroyAllWindows()