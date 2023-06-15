import cv2 as cv
from simple_facerec import SimpleFacerec
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 10
raw_capture = PiRGBArray(camera, size=(320, 240))

time.sleep(2)

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    image = frame.array
    face_loc, face_name = sfr.detect_known_faces(image)
    
    flag= False
    
    for floc, name in zip(face_loc, face_name):
        y1, x2, y2, x1 = floc[0], floc[1], floc[2], floc[3]
        cv.putText(image, name, (x1, y1-20), cv.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
        
        if name == "Unknown":
            print("Invalid user")
        else:
            print("Hi", name,"welcome")
            flag= True  
            break  
        
        cv.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv.imshow("Frame", image)

    key = cv.waitKey(1)
    if key == ord('q') or flag:
        print("Face_ID Accepted")
        break 

    raw_capture.truncate(0)

camera.close()
cv.destroyAllWindows()
