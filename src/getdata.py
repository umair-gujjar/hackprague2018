

import cv2
frame_num = 30
frame_count = 0
camera = cv2.VideoCapture(0)
while True:
    frame_count += 1
    return_value,image = camera.read()
    flip = cv2.flip(image, 1)
    gray = cv2.cvtColor(flip,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if(frame_count>frame_num):
        frame_count = 0
        # give gray to the NN
    if cv2.waitKey(1)& 0xFF == ord('s'):
        break
camera.release()
cv2.destroyAllWindows()

