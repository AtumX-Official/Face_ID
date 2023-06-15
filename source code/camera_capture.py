import picamera
import os
import cv2 as cv
from picamera.array import PiRGBArray

save_folder = 'path/to/folder'
camera = picamera.PiCamera()
camera.resolution = (640, 480)
raw_capture = PiRGBArray(camera, size=(camera.resolution[0], camera.resolution[1]))
time.sleep(2)


for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    
    image = frame.array
    
    cv.imshow("Camera Feed", image)

   
    key = cv.waitKey(1) & 0xFF
    if key == ord('s'):
        name=input("enter name")
        
        image_path = os.path.join(save_folder, name+".jpg")
        cv.imwrite(image_path, image)
        print("Image saved successfully at:", image_path)
        break

    raw_capture.truncate(0)


camera.close()
cv.destroyAllWindows()
