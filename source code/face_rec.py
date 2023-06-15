import cv2 as cv
from simple_facerec import  SimpleFacerec

cap=cv.VideoCapture(2)
sfr=SimpleFacerec()
sfr.load_encoding_images("images/")

while True:
    ret,frame=cap.read()
    face_loc,face_name=sfr.detect_known_faces(frame)
    for floc,name in zip(face_loc,face_name):
        y1,x2,y2,x1=floc[0],floc[1],floc[2],floc[3]
        cv.putText(frame,name,(x1,y1-20),cv.FONT_HERSHEY_DUPLEX,2,(0,255,0),2)
        print("Hi",name )
        cv.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    cv.imshow("Frame",frame)
    key=cv.waitKey(1)
    if key==27:
        break
cap.release()
cv.destroyAllWindows()