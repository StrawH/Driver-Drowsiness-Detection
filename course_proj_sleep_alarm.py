#imported needed lib
import cv2
import pygame

# sound function
def playsound (var):
    if var == True:
        pygame.mixer.music.load("/home/omar/PycharmProjects/untitled1/drawsnis alarm/zz.wav")
        pygame.mixer.music.play()
        var== False

#face and eye classifires
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

#start live show
while True :
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    pygame.init()

#start reading face and coordinates
    for (x,y,w,h) in faces:

        #square_center = (int((x+w)),int((y+h)))
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.circle(img,(int((x+x+w)/2),int ((y+y+h)/2)),int((w)/2),(255,204,204),4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        #eye coordinates
        for (ex,ey,ew,eh) in eyes:
            eye_cordx= int ((ex+ex+ew)/2)
            eye_cordy= int ((ey+ey+eh)/2)
            # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
            cv2.circle(roi_color,(eye_cordx,eye_cordy),20,(0,255,0),2)

            #alarm when sleeping
            print(eyes)
            if  len(eyes) ==1 or  [] :
                cv2.putText(img, "Sleep ALERT! Eyes in not on road ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 204, 153), 2)
                playsound(True)

    #start prodcasting
    cv2.imshow('LIVE', img)

    #break when i tell you
    if cv2.waitKey(10) & 255 == ord('s'):
        break

#do not run in background
cv2.destroyAllWindows()