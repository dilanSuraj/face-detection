import cv2 as cv

cap = cv.VideoCapture(0)

# FourCC = cv.VideoWriter_fourcc('X', 'V', 'I', 'D')
# or
FourCC = cv.VideoWriter_fourcc(*'XVID')

#                       out put file, source, resolution, frame size
result = cv.VideoWriter('output.avi', FourCC, 20.0, (640, 480))

while(cap.isOpened()):

    ret, frame = cap.read()

    # check if it is captured
    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))

        # added to the result
        result.write(frame)

        cv.imshow("Frame", frame)

        if cv.waitKey(1) & 0xFF == ord('e'):
            break

cap.release()
result.release()
cv.destroyAllWindows()